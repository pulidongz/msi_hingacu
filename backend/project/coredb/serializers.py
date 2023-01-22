from rest_framework import serializers
from coredb.models import ALWANStation, ALWANSurvey


class ALWANSurveySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='coredb:alwansurvey-detail',
        lookup_field='pk'
    )

    class Meta:
        model = ALWANSurvey
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


class ALWANStationSerializer(serializers.ModelSerializer):
    surveys = ALWANSurveySerializer(source='alwansurvey_set', many=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='coredb:alwanstation-detail',
        lookup_field='pk'
    )
    #barangay
    barangay = serializers.SerializerMethodField('get_barangay')
    def get_barangay(self, obj):
        return obj.location.barangay
    #town
    town = serializers.SerializerMethodField('get_town')
    def get_town(self, obj):
        return obj.location.town
    #province
    province = serializers.SerializerMethodField('get_province')
    def get_province(self, obj):
        return obj.location.province

    class Meta:
        model = ALWANStation
        fields = [
            'url',
            'id',
            'name',
            'corner_1',
            'corner_2',
            'gps_datum',
            'barangay',
            'town',
            'province',
            'type_of_management',
            'additional_information',
            'surveys',
        ]

"""
class SurveyDetailSerializer(SurveySerializer):
    fish_report = serializers.SerializerMethodField('get_fish_report')
    invertebrate_report = serializers.SerializerMethodField('get_invertebrate_report')

    def get_fish_report(self, obj):
        return obj.generate_fish_report()

    def get_invertebrate_report(self, obj):
        return obj.generate_invertebrate_report()

    class Meta:
        model = ALWANSurvey
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

    class Meta:
        model = ALWANStation
        fields = [
            'url',
            'id',
            'code',
            'corner_1_lat',
            'corner_1_lon',
            'corner_2_lat',
            'corner_2_lon',
            'name',
            'location',
            'type_of_management',
            'additional_information',
        ]
"""