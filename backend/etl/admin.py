from django.contrib import admin
from django.db.models import JSONField
from jsoneditor.forms import JSONEditor
from etl.models import (ETLFile, ETLFileRow, DCPCollection,
    DataCapturePoint, GoogleDriveFile, KeyValueStore, ExtractedData,
    Workbook, WorkbookConfiguration, WorksheetConfiguration, DataExtractionConfiguration)


class ETLFileRowAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'project',
        'file_name',
        'sheet_name',
        'sheet_slug',
        'row',
        'date_created',
        'date_updated'
    )

    def code(self, obj):
        return obj.__str__()

    def file_name(self, obj):
        return obj.etlfile.get_filename()

    def row(self, obj):
        return obj.number

    def project(self, obj):
        return obj.etlfile.dcp_collection.name


class DataCapturePointAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField:{'widget': JSONEditor},
    }

    list_display = (
        'collection',
        'code',
        'label',
        'sheet_name',
    )


class DCPInline(admin.StackedInline):
    model = DataCapturePoint
    formfield_overrides = {
        JSONField:{'widget': JSONEditor},
    }
    extra = 0

class DCPCollectionAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'name'
    )
    inlines = [DCPInline,]

class GoogleDriveFileAdmin(admin.ModelAdmin):
    list_display = (
        'drive_url',
        'downloaded',
    )

class KeyValueStoreAdmin(admin.ModelAdmin):
    list_display = (
        'etlfile',
        'sheet_name',
        'code'
    )

class DataExtractionConfigurationInline(admin.StackedInline):
    model = DataExtractionConfiguration

class WorksheetConfigurationAdmin(admin.ModelAdmin):
   inlines = [DataExtractionConfigurationInline,]

# Register your models here.
admin.site.register(ETLFile)
admin.site.register(ExtractedData)
admin.site.register(ETLFileRow, ETLFileRowAdmin)
admin.site.register(DCPCollection, DCPCollectionAdmin)
admin.site.register(DataCapturePoint, DataCapturePointAdmin)
admin.site.register(GoogleDriveFile, GoogleDriveFileAdmin)
admin.site.register(KeyValueStore, KeyValueStoreAdmin)

admin.site.register(Workbook)
admin.site.register(WorkbookConfiguration)
admin.site.register(WorksheetConfiguration, WorksheetConfigurationAdmin)