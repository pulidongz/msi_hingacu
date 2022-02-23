from django.conf import settings
from etl.models import Workbook
from etl.workbooks.tasks import process_workbook


# task passed on to the task broker for loading etl files
def process(workbook_id):
    # query for the workbook then process it
    workbook = Workbook.objects.get(pk=workbook_id)
    try:
        process_workbook(workbook)
        if settings.DEBUG == True:
            raise Exception("TASK COMPLETE") # debug mode so I won't have to keep reuploading
    except Exception as e:
        workbook.status = Workbook.STATUS_FAILED
        workbook.save()
        if settings.DEBUG == True:
            raise Exception(str(e)) # debug mode so I won't have to keep reuploading
    return workbook.status


# return hook for process
def complete(task):
    if task.success:
        print("TASK COMPLETE", task.result)
    else:
        print("TASK FAILED", task.result)
