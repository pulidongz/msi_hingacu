from django.conf import settings
from etl.models import Workbook
from etl.workbooks.tasks import process_workbook


# task passed on to the task broker for loading etl files
def process(workbook_id):
    # query for the workbook then process it
    workbook = Workbook.objects.get(pk=workbook_id)
    process_workbook(workbook)
    return workbook.status


# return hook for process
def complete(task):
    if task.success:
        print("TASK COMPLETE", task.result)
    else:
        print("TASK FAILED", task.result)
