from django.conf import settings
from projects.constants import PROJECT_2, P201
from etl.models import ETLFile
from etl.forms import DCRForm, P202Form
from etl.scripts.core import ETLProcess


def process_project2(etlfile):
    # delete all proxy data related to file
    etlfile.errors = []
    etlfile.status = ETLFile.STATUS_PROCESSING
    etlfile.save()
    ProxyTaxonomicData.objects.filter(etlfile=etlfile).delete()
    ProxySpecimen.objects.filter(etlfile=etlfile).delete()

    # P201 - Acquisition
    process_0201(etlfile)
    # P202
    #process_0202(etlfile)

    if etlfile.errors:
        etlfile.status = ETLFile.STATUS_FAILED
    else:
        etlfile.status = ETLFile.STATUS_COMPLETED
    etlfile.save()
    raise Exception('STOP') # temporary


# PROJECT 2 - 01
def process_0201(etlfile):
    #define ETL process
    dcr = get_DCR(PROJECT_2, P201)
    sheet_name = dcr.sheet_name
    key_mapping = dcr.mapping
    if settings.DEBUG:
        print('DCR', dcr.sheet_name, dcr.mapping)
    form_class = DCRForm
    etlprocess = ETLProcess(sheet_name, key_mapping, form_class)
    etlprocess.extract(etlfile)


# PROJECT 2 - 02
def process_0202(etlfile):
    raw_specimens = etlfile.get_data(
        constants.P2_KEY_MAPPING_02,
        sheet_name=constants.P2_SHEET_2)
    row_index = 0
    for row in raw_specimens:
        row_index = row_index + 1;
        #print(row_index, row)
        form = P202Form(row)
        if form.is_valid():
            taxo, created = ProxyTaxonomicData.objects.get_or_create(
                    scientific_name=form.cleaned_data['scientific_name'],
                    etlfile=etlfile
                )
            specimen, created = ProxySpecimen.objects.get_or_create(
                collection_number=form.cleaned_data['collection_number'],
                etlfile=etlfile,
                defaults={
                    'taxonomic_lineage': taxo,
                    'collection_site': form.cleaned_data['collection_site'],
                    'collection_number': form.cleaned_data['collection_number'],
                    'collection_date': form.cleaned_data['collection_date']
                },
            )
            #print(created, form.cleaned_data)
        else:
            form_errors = form.errors.as_data()
            etlfile.add_errors(form_errors, row_index, constants.P3_SHEET_2)
            print("ERROR", etlfile.errors)

    if etlfile.errors:
        print("ERROR", etlfile.errors)
        etlfile.status = ETLFile.STATUS_FAILED
        etlfile.save()

