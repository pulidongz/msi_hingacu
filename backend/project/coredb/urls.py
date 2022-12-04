from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coredb import views

app_name = 'coredb'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'alwan-stations', views.ALWANStationViewSet)
router.register(r'alwan-surveys', views.ALWANSurveyViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.index, name='landing-page'),
    path('api/', include(router.urls)),
]