from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from etl import views

app_name = 'etl'
urlpatterns = [
    #path('', login_required(views.ETLFileListView.as_view()), name='etl-list'),
    #path('', lambda request: redirect('workbooks/', permanent=False)),
    path('upload/', login_required(views.UploadView.as_view()), name='etl-upload'),
    path('collection/<slug:pk>/', login_required(views.DCPCollectionDetailView.as_view()), name='collection-detail'),
    path('file/<int:pk>/', login_required(views.ETLFileDetailView.as_view()), name='etl-detail'),
    path('file/data/<int:etlfile_id>/<slug:sheet_name>/', login_required(views.ETLFileRowListView.as_view()), name='etl-row-list'),
    path('file/errors/<int:pk>/<slug:sheet_name>/', login_required(views.ETLFileErrorListView.as_view()), name='etl-error-list'),
    #workbooks
    path('', login_required(views.WorkbookListView.as_view()), name='workbook-list'),
    path('workbooks/upload/', login_required(views.WorkbookUploadView.as_view()), name='workbook-upload'),
    path('workbooks/<int:pk>/', login_required(views.WorkbookDetailView.as_view()), name='workbook-detail'),
    path('workbooks/', views.workbook_upload_select, name='workbook-upload-select'),
    path('workbooks/types', views.WorkbookLayoutListView.as_view(), name='workbook-layout-list'),
    path('workbooks/types/<int:pk>/', views.WorkbookLayoutDetailView.as_view(), name='workbook-layout-detail'),
]