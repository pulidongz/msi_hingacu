from openpyxl.utils.exceptions import InvalidFileException
from etl.models import Workbook, DataExtractionConfiguration


class ExtractProcess:
    # Generalized Process for Validating and Extracting Data from a worksheet

    def __init__(self, config, workbook):
        # assumption here is that the wb has already been checked to contain the config's requirements
        self.workbook = workbook
        self.config = config
        print(self.config)

    def extract(self):
        # Initialize Worksheet
        wb = self.workbook.get_workbook()
        sheet_name = self.config.sheet_name
        try:
            ws = wb[sheet_name]
        except KeyError:
            message = 'Sheet "' + sheet_name + '" does not exist.'
            raise Workbook.DoesNotExist(message)

        #Get data values based on config
        data = {}
        if self.config.extraction_type == DataExtractionConfiguration.TYPE_FORM:
            for field in self.config.rules['fields']:
                value = ws[field['cell']].value
                data[field['field_name']] = value

        print("RAW", data)
        return data

    def validate(self, data):
        # validate extracted data with given form_class

        rules = self.config.rules['fields']
        form_class = self.config.get_validation_form()

        form = form_class(data, rules=rules, file=self.workbook)
        result = {
            'data': None,
            'errors': None
        }
        if form.is_valid():
            result['data'] = form.cleaned_data
        else:
            result['errors'] = form.errors.as_data()
        return result

    def transform(self, data):
        # transform data in preparation for saving to database
        #print(data)
        return data

    def load(self, data):
        # save data into database
        print(data)

    def run(self):
        #extract raw data based on config
        raw_data = self.extract()

        #validate raw data based on config
        if self.config.extraction_type == DataExtractionConfiguration.TYPE_FORM:
            #validate entire raw data if form type in a single form
            results = self.validate(raw_data)

        #save results found into database
        data = self.transform(results)
        self.load(data)