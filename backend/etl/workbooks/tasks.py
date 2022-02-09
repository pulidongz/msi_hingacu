from django.conf import settings
from etl.models import Workbook


def process_workbook(workbook):
    # set work book status to 'PROCESSING' and reset errors field
    workbook.errors = []
    workbook.status = Workbook.STATUS_PROCESSING
    workbook.save()

    # initialize result workbook
    result_wb = workbook.load_workbook()

    # go through the configuration for this workbook and extract data in order
    sheet_configurations = workbook.configuration.get_sheet_configurations()
    print('CONFIG:', sheet_configurations)
    
    workbook.status = Workbook.STATUS_COMPLETED
    workbook.save()
