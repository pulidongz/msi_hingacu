from django.conf import settings
from etl.models import Workbook, ExtractedData, ExtractionError
from etl.workbooks.publisher import PublisherException


def process_workbook(workbook):
    # set work book status to 'PROCESSING' and reset errors field
    workbook.errors = []
    workbook.status = Workbook.STATUS_PROCESSING
    workbook.save()

    # delete all existing extracted data for workbook (start from 0)
    ExtractedData.objects.filter(workbook=workbook).delete()
    ExtractionError.objects.filter(workbook=workbook).delete()

    # go through the configuration for this workbook and extract data in order
    sheet_configurations = workbook.configuration.get_sheet_configurations()
    print('SHEET CONFIGS:', sheet_configurations)
    for sheet_config in sheet_configurations:
        #check if the sheet is present in workbook
        if not workbook.sheet_is_available(sheet_config.sheet_name):
            #add a file error then move on to the next config
            error_message = f"Missing sheet: {sheet_config.sheet_name}"
            print("FILE ERROR",error_message)
            workbook.add_file_error(error_message)
            continue
        #process the workbook for this worksheet if config has no issues
        process_worksheet(sheet_config, workbook)
    
    # check if any errors were recorded, update status, then save
    if workbook.has_errors():
        workbook.status = Workbook.STATUS_CORRECTIONS_NEEDED
        if workbook.has_field_errors():
            workbook.generate_checked_wb()
    else:
        workbook.status = Workbook.STATUS_COMPLETED
    workbook.save()

    if workbook.status == Workbook.STATUS_COMPLETED:
        #convert extracted data to schema tables if publisher is available
        publisher_class = workbook.configuration.get_publisher_class()
        if publisher_class:
            task = publisher_class(workbook)
            try:
                task.run()
            except PublisherException as e:
                workbook.add_file_error(str(e))
                workbook.status = Workbook.STATUS_CORRECTIONS_NEEDED
                workbook.save()



def process_worksheet(sheet_config, workbook):
    # go through each extraction task for the worksheet in the config
    extract_configs = sheet_config.get_extraction_configurations()
    for config in extract_configs:
        config.sheet_name = sheet_config.sheet_name #attach sheet name to etl config so it wont query again
        etl_class = config.get_etl_class()
        task = etl_class(config, workbook)
        task.run()