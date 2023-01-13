from django.conf import settings
from abc import ABCMeta, abstractmethod
from etl.models import DataExtractionConfiguration, ExtractedData


class PublisherException(Exception):
    pass

class PublisherProcess:
    # Generalized Process for converting clean extracted to schema tables
    __metaclass__ = ABCMeta

    def __init__(self, workbook):
        self.workbook = workbook

    def get_form_data(self, section_name):
        config = DataExtractionConfiguration.objects.get(
        	worksheet_configuration__workbook_configuration = self.workbook.configuration,
        	name=section_name)
        extracted_data = ExtractedData.objects.get(workbook=self.workbook, configuration=config)
        return extracted_data.data

    def get_table_data(self, section_name):
    	config = DataExtractionConfiguration.objects.get(
        	worksheet_configuration__workbook_configuration = self.workbook.configuration,
        	name=section_name)
    	return ExtractedData.objects.get(workbook=self.workbook, configuration=config)

    @abstractmethod
    def run(self):
        # for every entry create X
        pass

    def get_preview_context(self): #override for preview template
        return None