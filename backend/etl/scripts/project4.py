from django.conf import settings
from etl.models import ETLFile, ETLFileRow
from etl.forms import DCRForm
from etl.scripts.core import ETLProcess


def process_project4(etlfile):
    # delete all proxy data related to file
    etlfile.errors = []
    etlfile.status = ETLFile.STATUS_PROCESSING
    etlfile.save()

    # P401 - Acquisition
    process_0401(etlfile)
    process_0402(etlfile)
    process_0403(etlfile)
    process_0404(etlfile)

    if etlfile.errors:
        etlfile.status = ETLFile.STATUS_FAILED
    else:
        etlfile.status = ETLFile.STATUS_COMPLETED
    etlfile.save()

def process_0401(etlfile):
    dcr = get_DCR(PROJECT_4, P401)
    sheet_name = dcr.sheet_name
    key_mapping = dcr.mapping
    if settings.DEBUG:
        print('DCR', dcr.sheet_name, dcr.mapping)
    form_class = DCRForm
    etlprocess = ETLProcess(sheet_name, key_mapping, form_class)
    etlprocess.extract(etlfile)

def process_0402(etlfile):
    dcr = get_DCR(PROJECT_4, P402)
    sheet_name = dcr.sheet_name
    key_mapping = dcr.mapping
    if settings.DEBUG:
        print('DCR', dcr.sheet_name, dcr.mapping)
    form_class = DCRForm
    etlprocess = ETLProcess(sheet_name, key_mapping, form_class)
    etlprocess.extract(etlfile)

def process_0403(etlfile):
    dcr = get_DCR(PROJECT_4, P403)
    sheet_name = dcr.sheet_name
    key_mapping = dcr.mapping
    if settings.DEBUG:
        print('DCR', dcr.sheet_name, dcr.mapping)
    form_class = DCRForm
    etlprocess = ETLProcess(sheet_name, key_mapping, form_class)
    etlprocess.extract(etlfile)

def process_0404(etlfile):
    dcr = get_DCR(PROJECT_4, P404)
    sheet_name = dcr.sheet_name
    key_mapping = dcr.mapping
    if settings.DEBUG:
        print('DCR', dcr.sheet_name, dcr.mapping)
    form_class = DCRForm
    etlprocess = ETLProcess(sheet_name, key_mapping, form_class)
    etlprocess.extract(etlfile)