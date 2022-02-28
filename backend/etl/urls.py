from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from etl import views

app_name = 'etl'
urlpatterns = [
    path('', login_required(views.ETLFileListView.as_view()), name='etl-list'),
    path('upload/', login_required(views.UploadView.as_view()), name='etl-upload'),
    path('collection/<slug:pk>/', login_required(views.DCPCollectionDetailView.as_view()), name='collection-detail'),
    path('file/<int:pk>/', login_required(views.ETLFileDetailView.as_view()), name='etl-detail'),
    path('file/data/<int:etlfile_id>/<slug:sheet_name>/', login_required(views.ETLFileRowListView.as_view()), name='etl-row-list'),
    path('file/errors/<int:pk>/<slug:sheet_name>/', login_required(views.ETLFileErrorListView.as_view()), name='etl-error-list'),
    #workbooks
    path('workbooks/', login_required(views.WorkbookListView.as_view()), name='workbook-list'),
    path('workbooks/upload/', login_required(views.WorkbookUploadView.as_view()), name='workbook-upload'),
]