class ExtractProcess:
    # Generalized Process for Validating and Extracting Data from a worksheet

    def __init__(self, config, worksheet):
        self.worksheet = worksheet
        self.config = config
        self.form_class = dcp.get_validation_form()

    def extract(self):
        # Initialize Worksheet
        try:
            wb = self.etlfile.get_workbook()
            print('SHEET NAMES', wb.sheetnames)
            sheet_name = self.dcp.sheet_name
            try:
                ws = wb[sheet_name]
            except KeyError:
                message = 'Sheet "' + sheet_name + '" does not exist.'
                raise ETLFile.DoesNotExist(message)
        except InvalidFileException as e:
            raise e

        # Get worksheet value per field in DCP Configuration
        data = {}
        for field in self.requirements:
            cell_coordinate = field["field_cell"].split(":")[0] # only top left reference has value for merged cells
            cell = ws[cell_coordinate]
            print(cell)
            data[field["field_name"]] = cell.value

        return data

    def validate(self, data):
        # validate extracted data with given form_class

        dcr = {} # convert list to dict for now. TO DO: update DCRform to accept a list
        for requirement in self.requirements:
            dcr[requirement['field_name']] = requirement

        form = self.form_class(data, dcr=dcr, etlfile=self.etlfile)
        if form.is_valid():
            return form.cleaned_data
        else:
            return False

    def transform(self, data):
        # transform data in preparation for saving to database
        print(data)
        return data

    def load(self, data):
        # save data into database
        saved_data = ExtractedData.objects.create(
            etlfile = self.etlfile,
            sheet_name = self.dcp.sheet_name,
            data = data
        )

    def run(self):
        raw_data = self.extract()
        data = self.validate(raw_data)
        data = self.transform(data)
        self.load(data)