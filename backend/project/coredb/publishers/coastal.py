from decimal import Decimal
from django.contrib.gis.geos import Point
from etl.workbooks.publisher import PublisherProcess, PublisherException
from etl.models import DataExtractionConfiguration, ExtractedData
from coredb.models import Location, BeachProfileSurvey
from django.db import transaction


class BeachProfilePublisher(PublisherProcess):
    SITE_INFO_SECTION = "Survey Details"

    @transaction.atomic
    def run(self):
        wb = self.workbook

        if wb.status != wb.STATUS_COMPLETED:
            raise PublisherException("Workbook Extraction Not Completed!")

        survey_data = self.get_form_data(self.SITE_INFO_SECTION)

        #Get or create Location
        location, created = Location.objects.get_or_create(
            site_name = survey_data['site_name'].upper(),
            barangay = survey_data['barangay'].upper(),
            town = survey_data['town'].upper(),
            province = survey_data['province'].upper(),
        )

        #Get or Create bp survey
        lat = survey_data['start_lat']
        lon = survey_data['start_lon']
        print("COORD", lat, lon)
        corner_1 = Point(float(lon), float(lat), srid=4326) #point has (x,y) costructor
        lat = survey_data['end_lat']
        lon = survey_data['end_lon']
        print("COORD 2", lat, lon)
        corner_2 = Point(float(lon), float(lat), srid=4326)
        survey, created = BeachProfileSurvey.objects.get_or_create(
            transect_name = survey_data['transect_name'],
            location = location,
            start_point = corner_1,
            end_point = corner_2,
            date = survey_data['date'],
            start_time = survey_data['start_time'],
            end_time = survey_data['end_time'],
            team_leader_name = survey_data['team_leader_name'],
            defaults = {
                'workbook': self.workbook,
                'transect_orientation': survey_data['transect_orientation'],
                'description_of_fixed_point': survey_data['description_of_fixed_point'],
                'team_leader_contact_number': survey_data['team_leader_contact_number'],
                'team_leader_affiliation': survey_data['team_leader_affiliation'],
                'time_at_waterline': survey_data['time_at_waterline'],
                'point_at_waterline': survey_data['point_at_waterline'],
                #'tide_level': survey_data['tide_level'],
                #'mtl': survey_data['mtl']
            }
        )


        if not created: #stop if this survey already exists (remove if overwrites are allowed)
            raise PublisherException("Beach Profile Survey already exists")


    def get_preview_context(self):
        include_template = 'coredb/beach_preview.html'
        survey = BeachProfileSurvey.objects.get(workbook=self.workbook)
        context = {
            'template': include_template,
            'workbook': self.workbook,
            'survey': survey,
        }
        print(survey.start_point)
        return context