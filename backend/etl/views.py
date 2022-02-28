from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_q.tasks import async_task, result, fetch
from django_q.models import Task
from etl.models import ETLFile, ETLFileRow, DCPCollection, DataCapturePoint, Workbook
from etl.forms import ETLFileForm


class UploadView(LoginRequiredMixin, CreateView):
    model = ETLFile
    fields = ['dcp_collection', 'file']
    success_url = '/etl/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploader = self.request.user
        self.object.save() #get pk
        #create a task to process this ETL File
        task_id = async_task(
            'etl.scripts.process',
            self.object.pk,
            hook='etl.scripts.complete')
        #associate task to file
        self.object.task_id = task_id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class WorkbookUploadView(LoginRequiredMixin, CreateView):
    model = Workbook
    fields = ['file', 'configuration']
    success_url = '/etl/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploader = self.request.user
        self.object.save() #get pk
        self.object.process() #start async process for workbook
        return HttpResponseRedirect(self.get_success_url())


class WorkbookListView(LoginRequiredMixin, ListView):
    model = Workbook
    paginate_by = 5  # if pagination is desired
    ordering = ['-date_created']

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return Workbook.objects.filter(uploader=self.request.user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = ETLFileForm()
        context['dcp_collections'] = DCPCollection.objects.all()
        return context


class ETLFileListView(LoginRequiredMixin, ListView):
    model = ETLFile
    paginate_by = 5  # if pagination is desired
    ordering = ['-date_created']

    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        return ETLFile.objects.filter(uploader=self.request.user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = ETLFileForm()
        context['dcp_collections'] = DCPCollection.objects.all()
        return context


class ETLFileDetailView(LoginRequiredMixin, DetailView):
    model = ETLFile

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a extra context
        extracted_data = ETLFileRow.objects.filter(etlfile=self.object)
        if extracted_data:
            summary = {
                'error_count': len(self.object.errors),
                'rows_extracted': extracted_data.count(),
            }
            context['summary'] = summary
            context['data_per_dcp'] = extracted_data
            context['dcps'] = self.object.get_report()
        context['form'] = ETLFileForm()
        return context


class DCPCollectionDetailView(LoginRequiredMixin, DetailView):
    model = DCPCollection

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a extra context
        context['dcps'] = DataCapturePoint.objects.filter(collection=self.object)
        return context



class ETLFileRowListView(LoginRequiredMixin, ListView):
    model = ETLFileRow
    paginate_by = 20  # if pagination is desired
    ordering = ['number']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        etlfile_id = self.kwargs['etlfile_id']
        context['etlfile'] = ETLFile.objects.get(pk=etlfile_id)
        return context

    def get_queryset(self):
        etlfile_id = self.kwargs['etlfile_id']
        sheet_name = self.kwargs['sheet_name']
        return ETLFileRow.objects.filter(etlfile=etlfile_id, sheet_slug=sheet_name).order_by('number')


class ETLFileErrorListView(LoginRequiredMixin, DetailView):
    model = ETLFile
    template_name = 'etl/etlfile_error_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sheet_name = self.kwargs['sheet_name']
        try:
            context['error_list'] = self.object.get_errors()[sheet_name]
        except KeyError:
            pass
        return context
