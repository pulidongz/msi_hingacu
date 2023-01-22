from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from rest_framework import viewsets
from coredb.models import ALWANStation, ALWANSurvey
from coredb.serializers import (ALWANSurveySerializer, ALWANStationSerializer)

## NORMAL VIEWS

def index(request):
    context = {}
    #response = redirect('/accounts/login')
    #return response
    return render(request, 'index.html', context)

def logged_in_message(sender, user, request, **kwargs):
    """
    Add a welcome message when the user logs in
    """
    message = "Welcome, you are logged in as <b>{{ user.email }}</b>!"
    messages.success(request, message)

#user_logged_in.connect(logged_in_message)


## API VIEWS


class ALWANStationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing Stations.
    """
    queryset = ALWANStation.objects.filter()
    serializer_class = ALWANStationSerializer

#    def get_serializer(self, *args, **kwargs):
#        """
#        Return the serializer instance that should be used for validating and
#        deserializing input, and for serializing output.
#        """
#        if 'many' in kwargs.keys():
#            serializer_class = StationSerializer
#        else:
#            serializer_class = self.get_serializer_class()
#        kwargs.setdefault('context', self.get_serializer_context())
#        return serializer_class(*args, **kwargs)


class ALWANSurveyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing AL1 survey results.
    """
    queryset = ALWANSurvey.objects.filter()
    serializer_class = ALWANSurveySerializer

    #def get_serializer(self, *args, **kwargs):
    #    """
    #    Return the serializer instance that should be used for validating and
    #    deserializing input, and for serializing output.
    #    """
    #    if 'many' in kwargs.keys():
    #        serializer_class = SurveySerializer
    #    else:
    #        serializer_class = self.get_serializer_class()
    #    kwargs.setdefault('context', self.get_serializer_context())
    #    return serializer_class(*args, **kwargs)
