from django.conf import settings
from etl.models import ETLFile
from etl.scripts.core import process_etlfile
#from etl.scripts.project2 import process_project2
#from etl.scripts.project3 import process_project3
#from etl.scripts.project4 import process_project4


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
