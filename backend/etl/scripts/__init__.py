from django.conf import settings
from etl.models import ETLFile
from etl.scripts.core import process_etlfile


# task passed on to the task broker for loading etl files
def process(etlfile_id):
    etlfile = ETLFile.objects.get(pk=etlfile_id)

    process_etlfile(etlfile)

    if settings.DEBUG == True:
        raise Exception('STOP FOR DEBUG') # debug mode so I won't have to keep reuploading
    return etlfile.processed


# return hook for process
def complete(task):
    print('Task Complete', task)
