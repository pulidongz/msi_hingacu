from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coredb import views

app_name = 'coredb'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'stations', views.StationViewSet)
router.register(r'surveys', views.SurveyViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]