from django.shortcuts import render
from rest_framework import viewsets
from coredb.models import Station, AL1Survey
from coredb.serializers import StationSerializer, SurveySerializer, ListSurveySerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Stations.
    """
    queryset = Station.objects.filter()
    serializer_class = StationSerializer


class SurveyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing AL1 survey results.
    """
    queryset = AL1Survey.objects.filter()
    serializer_class = SurveySerializer

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if 'many' in kwargs.keys():
            serializer_class = ListSurveySerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)
