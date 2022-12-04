from django.contrib import admin
from django.db.models import JSONField
from jsoneditor.forms import JSONEditor
from etl.models import (ETLFile, ETLFileRow, DCPCollection,
    DataCapturePoint, GoogleDriveFile, KeyValueStore, ExtractedData,
    Workbook, WorkbookConfiguration, WorksheetConfiguration, DataExtractionConfiguration, DataField,
    ExtractionError)


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

class ExtractedDataAdmin(admin.ModelAdmin):
    list_display = (
        'workbook',
        'configuration',
        'entry_number',
        'data',
    )

class ExtractionErrorAdmin(admin.ModelAdmin):
    list_display = (
        'workbook',
        'configuration',
        'field_name',
        'error',
        'entry_number'
    )

# WORKBOOK CONFIGURATION
class WorksheetConfigurationInline(admin.StackedInline):
    model = WorksheetConfiguration
    extra = 0


class WorkbookConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'version',
        'component'
    )

    inlines = [WorksheetConfigurationInline,]


# WORKSHEET CONFIGURATION
class DataExtractionConfigurationInline(admin.StackedInline):
    model = DataExtractionConfiguration
    extra = 0

class WorksheetConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        'sheet_name',
        'workbook_configuration',
    )
    inlines = [DataExtractionConfigurationInline,]


# WORKSHEET SECTION
class DataFieldInline(admin.StackedInline):
    model = DataField
    extra = 0

class DataExtractionConfigurationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_sheet_name',
        'get_workbook_name',
        'section_order',
        'extraction_type'
    )
    formfield_overrides = {
        JSONField:{'widget': JSONEditor},
    }
    inlines = [DataFieldInline,]

    def get_sheet_name(self, obj):
        return obj.worksheet_configuration.sheet_name
    get_sheet_name.admin_order_field = "worksheet_configuration"
    get_sheet_name.short_description = "sheet name"

    def get_workbook_name(self, obj):
        return obj.worksheet_configuration.workbook_configuration.name
    get_workbook_name.admin_order_field = "worksheet_configuration__workbook_configuration"
    get_workbook_name.short_description = "workbook type"

# Register your models here.
#admin.site.register(ETLFile)
#admin.site.register(ETLFileRow, ETLFileRowAdmin)
#admin.site.register(DCPCollection, DCPCollectionAdmin)
#admin.site.register(DataCapturePoint, DataCapturePointAdmin)
#admin.site.register(GoogleDriveFile, GoogleDriveFileAdmin)
#admin.site.register(KeyValueStore, KeyValueStoreAdmin)

admin.site.register(ExtractedData, ExtractedDataAdmin)
admin.site.register(Workbook)
admin.site.register(WorkbookConfiguration, WorkbookConfigurationAdmin)
admin.site.register(WorksheetConfiguration, WorksheetConfigurationAdmin)
admin.site.register(DataExtractionConfiguration, DataExtractionConfigurationAdmin)
admin.site.register(ExtractionError, ExtractionErrorAdmin)