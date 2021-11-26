from rest_framework import serializers
from coredb.models import Station


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'code',
            'start_point_lat',
            'start_point_lon',
            'end_point_lat',
            'end_point_lon',
            'reef_name',
            'barangay',
            'town',
            'province',
            'type_of_management',
            'additional_information',
            'curated'
        ]