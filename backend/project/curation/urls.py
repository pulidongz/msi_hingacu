from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from curation import views

app_name = 'curation'
urlpatterns = [
    path('', views.WorkbookCurationListView.as_view(), name='curation-list'),
    path('curate/', views.CurationCreateView.as_view(), name='curation-create')
]