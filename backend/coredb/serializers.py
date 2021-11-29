from rest_framework import serializers
from coredb.models import Station, AL1Survey


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

class ListSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = AL1Survey
        fields = [
            'code',
            'station',
            'date',
            'time',
            'team_leader',
            'team_scientist',
        ]

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = AL1Survey
        fields = [
            'code',
            'station',
            'date',
            'time',
            'team_leader',
            'team_scientist',
            'fish_counts',
        ]

    def get_fish_counts(self, obj):
        return obj.fish_counts()