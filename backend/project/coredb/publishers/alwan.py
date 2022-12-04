from decimal import Decimal
from django.contrib.gis.geos import Point
from etl.workbooks.publisher import PublisherProcess, PublisherException
from etl.models import DataExtractionConfiguration, ExtractedData
from coredb.models import ALWANStation, ALWANSurvey, Location
from django.db import transaction


class ALWANPublisher(PublisherProcess):
    SITE_INFO_SECTION = "Survey Information"

    @transaction.atomic
    def run(self):
        wb = self.workbook

        if wb.status != wb.STATUS_COMPLETED:
            raise PublisherException("Workbook Extraction Not Completed!")

        survey_data = self.get_form_data(self.SITE_INFO_SECTION)

        #Get or create Location
        location, created = Location.objects.get_or_create(
            site_name = survey_data['station_name'].upper(),
            barangay = survey_data['barangay'].upper(),
            town = survey_data['town'].upper(),
            province = survey_data['province'].upper(),
        )

        #Get or Create ALWAN Station
        lat, lon = survey_data['corner_1_coordinate'].split(',')
        print("COORD", lat, lon)
        corner_1 = Point(float(lon), float(lat), srid=4326) #point has (x,y) costructor
        lat, lon = survey_data['corner_2_coordinate'].split(',')
        print("COORD 2", lat, lon)
        corner_2 = Point(float(lon), float(lat), srid=4326)
        station, created = ALWANStation.objects.get_or_create(
            name = survey_data['station_name'],
            location = location,
            corner_1 = corner_1,
            corner_2 = corner_2,
            defaults = {
                'gps_datum': survey_data['gps_datum'],
                'additional_information': survey_data['additional_information'],
                'type_of_management': survey_data['type_of_management']
            }
        )

        survey, created = ALWANSurvey.objects.get_or_create(
            date = survey_data['survey_date'],
            time = survey_data['survey_time'],
            station = station,
            team_leader_name = survey_data['team_leader_name'],
            defaults = {
                'workbook': self.workbook,
                'team_leader_contact_number': survey_data['team_leader_contact_number'],
                'team_scientist_name': survey_data['team_scientist_name'],
                'volunteer_1': survey_data['volunteer_1'],
                'volunteer_2': survey_data['volunteer_2'],
                'volunteer_3': survey_data['volunteer_3'],
                'volunteer_4': survey_data['volunteer_4'],
                'volunteer_5': survey_data['volunteer_5'],
                'volunteer_6': survey_data['volunteer_6'],
            }
        )

        if not created: #stop if this survey already exists (remove if overwrites are allowed)
            raise PublisherException("ALWANSurvey already exists")




    def get_preview_context(self):
        include_template = 'coredb/alwan_preview.html'
        survey = ALWANSurvey.objects.get(workbook=self.workbook)
        station = survey.station
        context = {
            'template': include_template,
            'workbook': self.workbook,
            'station': station,
            'survey': survey,
        }
        print(station)
        print(station.corner_1.coords)
        print(station.corner_1_lat)
        return context