from django.conf import settings
from etl.models import Workbook


def process_workbook(workbook):
    # set work book status to 'PROCESSING' and reset errors field
    workbook.errors = []
    workbook.status = Workbook.STATUS_PROCESSING
    workbook.save()

    # initialize result workbook
    result_wb = workbook.get_workbook()

    # go through the configuration for this workbook and extract data in order
    sheet_configurations = workbook.configuration.get_sheet_configurations()
    print('CONFIG:', sheet_configurations)
    for sheet_config in sheet_configurations:
        #check if the sheet is present in workbook
        if not workbook.sheet_is_available(sheet_config.sheet_name):
            #add a file error then move on to the next config
            error_message = f"Missing sheet: {sheet_config.sheet_name}"
            workbook.add_file_error(error_message)
            continue
        #process the workbook for this worksheet if config has no issues
        process_worksheet(sheet_config, workbook)
    
    workbook.status = Workbook.STATUS_COMPLETED
    workbook.save()


def process_worksheet(sheet_config, workbook):
    # go through each extraction task for the worksheet in the config
    etl_task_configs = sheet_config.get_extraction_configurations()
    for etl_config in etl_task_configs:
        etl_config.sheet_name = sheet_config.sheet_name #attach sheet name to etl config so it wont query again
        etl_class = etl_config.get_etl_class()
        task = etl_class(etl_config, workbook)
        task.run()