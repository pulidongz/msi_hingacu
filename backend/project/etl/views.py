from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_q.tasks import async_task, result, fetch
from django_q.models import Task
from etl.models import ETLFile, ETLFileRow, DCPCollection, DataCapturePoint, Workbook, WorkbookConfiguration, ExtractedData
from etl.forms import ETLFileForm
from curation.forms import CurationForm


class WorkbookUploadView(LoginRequiredMixin, CreateView):
    model = Workbook
    fields = ['file', 'configuration']
    success_url = '/etl/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploader = self.request.user
        self.object.save() #get pk
        self.object.process() #start async process for workbook
        return HttpResponseRedirect(self.get_success_url()+'?code='+self.object.configuration.code)

    #def dispatch(self, request, *args, **kwargs):
    #    code = self.request.GET.get('code', None)
    #    if code is None:
    #        return redirect('etl:workbook-list')
    #    return super(WorkbookUploadView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        code = self.request.GET.get('code', None)
        if code:
            context['configuration'] = WorkbookConfiguration.objects.get(code=code)
        return context


class AttachmentUploadView(LoginRequiredMixin, UpdateView):
    model = Workbook
    fields = ['attachments']
    template_name_suffix = '_update_form'


class WorkbookListView(LoginRequiredMixin, ListView):
    model = Workbook
    paginate_by = 20  # if pagination is desired
    ordering = ['-date_created']

    def get_queryset(self):
        code = self.request.GET.get('code', None)
        if self.request.user.is_staff:
            return super().get_queryset().order_by('-date_created')
        if code:
            return Workbook.objects.filter(
                configuration__code=code,
                uploader=self.request.user
            ).order_by('-date_created')
        return Workbook.objects.filter(uploader=self.request.user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        code = self.request.GET.get('code', None)
        if code:
            context['configuration'] = WorkbookConfiguration.objects.get(code=code)
        return context


class WorkbookDetailView(LoginRequiredMixin, DetailView):
    model = Workbook

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Show preview if available in publisher class
        publisher_class = self.object.configuration.get_publisher_class()
        if self.object.is_complete():
            if publisher_class:
                publisher = publisher_class(self.object)
                try:
                    context['preview'] = publisher.get_preview_context()
                    print("PREVIEW", context['preview'])
                except Exception as e:
                    print("PREVIEW ERROR", e)
        # Add in a extra context
        context['sheets'] = self.object.get_organized_extracted_data()
        # include a curation form
        context['curation_form'] = CurationForm({'workbook':self.object})
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


def workbook_upload_select(request):
    coastal = WorkbookConfiguration.objects.filter(component="Coastal Integrity")
    mangrove = WorkbookConfiguration.objects.filter(component="Mangrove Assessment")
    seagrass = WorkbookConfiguration.objects.filter(component="Seagrass Assessment")
    reef = WorkbookConfiguration.objects.filter(component="Reef Assessment")
    return render(request, 'etl/workbook_select.html', {
        'coastal': coastal,
        'mangrove': mangrove,
        'seagrass': seagrass,
        'reef': reef,
    })


class WorkbookLayoutListView(LoginRequiredMixin, ListView):
    model = WorkbookConfiguration
    paginate_by = 20  # if pagination is desired
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class WorkbookLayoutDetailView(LoginRequiredMixin, DetailView):
    model = WorkbookConfiguration

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a extra context
        config = self.object
        sheets = []
        for sheet in config.worksheetconfiguration_set.order_by('sheet_order'):
            sections = sheet.dataextractionconfiguration_set.order_by('section_order')
            section_list = []
            for section in sections:
                fields = section.datafield_set.all()
                section_list.append({
                        "section": section,
                        "fields": fields,
                    })
            sheets.append({
                "sheet_name": sheet.sheet_name,
                "sections": section_list
            })
        context["sheets"] = sheets
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
