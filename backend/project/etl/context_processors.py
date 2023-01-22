from django.conf import settings
from etl.models import WorkbookConfiguration


def workbook_configurations(request):
    configs = WorkbookConfiguration.objects.all().order_by('name')

    return {
        "configs": configs,
    }