from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from etl.models import Workbook
from curation.models import Curation, Curator


class WorkbookCurationListView(LoginRequiredMixin, ListView):
    model = Workbook
    paginate_by = 20  # if pagination is desired
    ordering = ['-date_created']
    template_name='curation/workbook_list.html'

    def get_queryset(self):
        #workbooks that only passed initial validation
        return Workbook.objects.filter(status=Workbook.STATUS_COMPLETED).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curated_list'] = Curation.objects.all()
        return context


class CurationCreateView(LoginRequiredMixin, CreateView):
    model = Curation
    fields = ['workbook', 'verdict', 'reason']
    success_url = '/curation/'

    def form_valid(self, form):
        try:
            curator = Curator.objects.get(user=self.request.user)
        except Curator.DoesNotExist as e:
            if self.request.user.is_staff:
                curator = Curator.objects.create(user=self.request.user)
            else:
                raise e
        form.instance.verdict_by = Curator.objects.get(user=self.request.user)
        return super().form_valid(form)
