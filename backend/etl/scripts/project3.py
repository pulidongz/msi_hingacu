from projects import constants
from etl.models import ETLFile


def process_project3(etlfile):
    # delete all proxy data related to file
    etlfile.errors = []
    etlfile.status = ETLFile.STATUS_PROCESSING
    etlfile.save()
    ProxyTaxonomicData.objects.filter(etlfile=etlfile).delete()
    ProxySpecimen.objects.filter(etlfile=etlfile).delete()
    ProxyExtract.objects.filter(etlfile=etlfile).delete()
    # P301 - Requests
    # process_0301(etlfile) skip. no data.
    # P302 - Specimens
    process_0302(etlfile)
    # P303 - Extracts
    process_0303(etlfile)
    # P304 - Releases
    process_0304(etlfile)
    # P305 - Stability Tests
    process_0305(etlfile)

    if etlfile.errors:
        etlfile.status = ETLFile.STATUS_FAILED
    else:
        etlfile.status = ETLFile.STATUS_COMPLETED
    etlfile.save()
    raise Exception('STOP') # temporary


def process_0301(etlfile):
    raw_data = etlfile.get_data(
        constants.P3_KEY_MAPPING_01,
        sheet_name=constants.P3_SHEET_1)


# PROJECT 3 - 02
def process_0302(etlfile):
    raw_specimens = etlfile.get_data(
        constants.P3_KEY_MAPPING_02,
        sheet_name=constants.P3_SHEET_2)
    row_index = 0
    for row in raw_specimens:
        row_index = row_index + 1;
        #print(row_index, row)
        form = P302Form(row)
        if form.is_valid():
            common_names = [name.strip() for name in form.cleaned_data['common_name'].split(',')]
            taxo, created = ProxyTaxonomicData.objects.get_or_create(
                    scientific_name=form.cleaned_data['scientific_name'],
                    etlfile=etlfile
                )
            specimen, created = ProxySpecimen.objects.get_or_create(
                code=form.cleaned_data['specimen_code'],
                etlfile=etlfile,
                defaults={
                    'date_received': form.cleaned_data['date_received'],
                    'plant_part': form.cleaned_data['plant_part'],
                    'taxonomic_lineage': taxo,
                    'form': form.cleaned_data['form'],
                    'picture': form.cleaned_data['picture'],
                    'accession_number': form.cleaned_data['accession_number'],
                    'collection_code': form.cleaned_data['collection_code'],
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
        #raise Exception('P302 VALIDATION FAILED')


# PROJECT 3 - 03
def process_0303(etlfile):
    raw_extracts = etlfile.get_data(
        constants.P3_KEY_MAPPING_03,
        sheet_name=constants.P3_SHEET_3)
    row_index = 0
    for row in raw_extracts:
        row_index = row_index + 1;
        #print(row_index, row)
        form = P303Form(row)
        if form.is_valid():
            try:
                specimen = ProxySpecimen.objects.get(code=form.cleaned_data['specimen_code'])
                extract, created = ProxyExtract.objects.get_or_create(
                    specimen=specimen,
                    code_1d=form.cleaned_data['code_1d'],
                    etlfile=etlfile
                )
                #print(created, form.cleaned_data)
            except ProxySpecimen.DoesNotExist as e:
                e.message = 'Specimen ' + form.cleaned_data['specimen_code'] + ' does not exist.'
                etlfile.add_errors({'specimen_code':[e]}, row_index, constants.P3_SHEET_3)
        else:
            form_errors = form.errors.as_data()
            etlfile.add_errors(form_errors, row_index, constants.P3_SHEET_3)

    if etlfile.errors:
        print("ERROR", etlfile.errors)
        etlfile.status = ETLFile.STATUS_FAILED
        etlfile.save()
        #raise Exception('P303 VALIDATION FAILED')


# PROJECT 3 - 04
def process_0304(etlfile):
    raw_data = etlfile.get_data(
        constants.P3_KEY_MAPPING_04,
        sheet_name=constants.P3_SHEET_4)


# PROJECT 3 - 05
def process_0305(etlfile):
    raw_data = etlfile.get_data(
        constants.P3_KEY_MAPPING_05,
        sheet_name=constants.P3_SHEET_5)

