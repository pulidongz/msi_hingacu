from django.shortcuts import render
from rest_framework import viewsets
from coredb.models import Station
from coredb.serializers import StationSerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Stations.
    """
    queryset = Station.objects.filter(curated=True)
    serializer_class = StationSerializer

