from rest_framework import serializers
from coredb.models import Station, AL1Survey

class SurveySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='coredb:al1survey-detail',
        lookup_field='pk'
    )

    class Meta:
        model = AL1Survey
        fields = [
            'url',
            'pk',
            'code',
            'station',
            'date',
            'time',
            'team_leader',
            'team_scientist',
            'curated',
        ]

class SurveyDetailSerializer(SurveySerializer):
    fish_report = serializers.SerializerMethodField('get_fish_report')
    invertebrate_report = serializers.SerializerMethodField('get_invertebrate_report')

    def get_fish_report(self, obj):
        return obj.generate_fish_report()

    def get_invertebrate_report(self, obj):
        return obj.generate_invertebrate_report()

    class Meta:
        model = AL1Survey
        fields = [
            'url',
            'id',
            'code',
            'station',
            'date',
            'time',
            'team_leader',
            'team_scientist',
            'curated',
            'fish_report',
            'invertebrate_report'
        ]


class StationSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='coredb:station-detail',
        lookup_field='pk'
    )
    survey_count = serializers.SerializerMethodField('get_survey_count')
    survey_count_curated = serializers.SerializerMethodField('get_survey_count_curated')

    def get_survey_count(self, obj):
        return obj.get_survey_count()

    def get_survey_count_curated(self, obj):
        return obj.get_survey_count(curated=True)

    class Meta:
        model = Station
        fields = [
            'url',
            'id',
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
            'curated',
            'survey_count',
            'survey_count_curated'
        ]


class StationDetailSerializer(StationSerializer):
    surveys = SurveySerializer(source='al1survey_set', many=True)

    class Meta:
        model = Station
        fields = [
            'url',
            'id',
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
            'curated',
            'survey_count',
            'survey_count_curated',
            'surveys',
        ]
