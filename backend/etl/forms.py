import datetime, json
from django import forms
from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from etl.models import ETLFile, ETLFileRow, KeyValueStore


class CleanDateField(forms.DateField):

    #def __init__(self, *, input_formats=None, **kwargs):
    #    super().__init__(**kwargs)
    #    if input_formats is not None:
    #        self.input_formats = input_formats
    #        self.input_formats = self.input_formats + '%Y%m%d'
    #        self.input_formats = self.input_formats + '%Y-%m-%d'
    #        self.input_formats = self.input_formats + '%Y/%m/%d'

    def to_python(self, value):
        """
        Validate that the input can be converted to a date. Return a Python
        datetime.date object.
        """
        if value in self.empty_values:
            return None
        if isinstance(value, datetime.datetime):
            return value.date()
        if isinstance(value, datetime.date):
            return value
        if type(value) != str: #cast non string values to string
                value = str(value)
        return super().to_python(value)


class ScientificNameField(forms.CharField):
    """
    Validates if a value for scientific name can be found in TaxonomicLineage table.
    """
    def to_python(self, value):
        if value in self.empty_values:
            return None
        TaxonomicLineage = apps.get_model('biorepository', 'TaxonomicLineage')
        try:
            TaxonomicLineage.objects.get(scientific_name__iexact=value)
        except (ValueError, TypeError, TaxonomicLineage.DoesNotExist):
            error_message = f"{value} has no entry in supplementary data for Taxonomic Lineages."
            raise ValidationError(
                error_message,
                code='invalid',
                params={'value': value},
            )
        return value


class ModelField(forms.CharField):
    """
    Validates if a value for a field can be found in a given model look up.
    """

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        self.app = kwargs.pop('app', None)
        self.query_field = kwargs.pop('query_field')
        super(ModelField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in self.empty_values:
            return None
        Model = apps.get_model(self.app, self.model)
        try:
            query = {self.query_field: value}
            Model.objects.get(**query)
        except (ValueError, TypeError, Model.DoesNotExist):
            error_message = f"{value} has no entry in {self.model} table."
            raise ValidationError(
                error_message,
                code='invalid',
                params={'value': value},
            )
        return value


class KeyLookUpField(forms.CharField):
    """
    Validates if a value for a field can be found in a key value store look up.
    """

    def __init__(self, *args, **kwargs):
        self.etlfile = kwargs.pop('etlfile', None)
        self.sheet_name = kwargs.pop('sheet_name', None)
        self.code = kwargs.pop('code', None)
        super(KeyLookUpField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in self.empty_values:
            return None
        key_store = KeyValueStore.objects.get(
            etlfile=self.etlfile,
            sheet_name=self.sheet_name,
            code=self.code)
        try:
            key_store.data[value]
        except KeyError:
            error_message = f"{value} has no valid record found in {self.sheet_name}."
            raise ValidationError(
                error_message,
                code='invalid',
                params={'value': value},
            )
        return value


class ETLFileForm(forms.ModelForm):
    class Meta:
        model = ETLFile
        fields = ['dcp_collection', 'file']


class DCRForm(forms.Form):
    #Dynamic Form that creates validation fields based on the current Project DCR Configuration
    #field_name: {column_name: string_value, field_type: string_value , required: boolean_value]

    def __init__(self, *args, **kwargs):
        self.warnings = []
        self.dcr = kwargs.pop('dcr')
        self.etlfile = kwargs.pop('etlfile')
        self.key_value_fields = {}

        super(DCRForm, self).__init__(*args, **kwargs)

        for field in self.dcr.keys():
            if self.dcr[field]['field_type'] == 'string' or self.dcr[field]['field_type'] == 'text':
                self.fields[field] = forms.CharField(required=self.dcr[field]['required'])
            elif self.dcr[field]['field_type'] == 'integer':
                self.fields[field] = forms.IntegerField(required=self.dcr[field]['required'])
            elif self.dcr[field]['field_type'] == 'decimal' or self.dcr[field]['field_type'] == 'numeric':
                self.fields[field] = forms.DecimalField(required=self.dcr[field]['required'])
            elif self.dcr[field]['field_type'] == 'date':
                input_formats = ['%Y%m%d', '%Y-%m-%d', '%Y/%m/%d']
                self.fields[field] = CleanDateField(required=self.dcr[field]['required'], input_formats=input_formats)
            elif self.dcr[field]['field_type'] == 'boolean':
                self.fields[field] = forms.BooleanField(required=self.dcr[field]['required'])
            elif self.dcr[field]['field_type'] == 'scientific_name':
                self.fields[field] = ScientificNameField(required=self.dcr[field]['required'])
            elif self.dcr[field]['field_type'] == 'model':
                app = self.dcr[field]['app']
                model = self.dcr[field]['model']
                query_field = self.dcr[field]['query_field']
                self.fields[field] = ModelField(required=self.dcr[field]['required'],
                    model=model, app=app, query_field=query_field)
            elif self.dcr[field]['field_type'] == 'key_value':
                self.fields[field] = forms.CharField(required=self.dcr[field]['required'])
                self.key_value_fields[field] = self.dcr[field]['value_field']
            elif self.dcr[field]['field_type'] == 'key_look_up':
                etlfile = self.etlfile
                self.fields[field] = KeyLookUpField(
                    required=self.dcr[field]['required'],
                    etlfile=self.etlfile,
                    sheet_name=self.dcr[field]['sheet_name'],
                    code=self.dcr[field]['code'])
            else:
                print('Missing field_type', field)
                self.fields[field] = forms.CharField(required=self.dcr[field]['required'])

    def clean(self):
        cleaned_data = super(DCRForm, self).clean()
        for field in self.dcr.keys():
            if 'required_soft' in self.dcr[field]:
                try:
                    if cleaned_data[field] is None:
                        self.warnings.append(field)
                except KeyError:
                    self.warnings.append(field)
        cleaned_data['WARNINGS'] = self.warnings
        return cleaned_data

    def save(self, sheet_name, row_index):
        cleaned_data = self.cleaned_data
        warnings = cleaned_data.pop('WARNINGS')
        
        # temporary since Decimal has trouble being encoded into JSON via the JSON model field
        # dump cleaned data as json string
        json_data = json.dumps(
            cleaned_data,
            sort_keys=True,
            indent=1,
            cls=DjangoJSONEncoder)

        row_data = ETLFileRow.objects.create(
            number=row_index,
            sheet_name=sheet_name,
            etlfile=self.etlfile,
            data=json_data,
            warnings=warnings
        )

        for field in self.key_value_fields.keys():
            key_store, created = KeyValueStore.objects.get_or_create(
                code = self.dcr[field]['code'],
                etlfile = self.etlfile,
                sheet_name = sheet_name,
            )
            mapping = key_store.data if key_store.data else {}
            key = cleaned_data[field]
            value = cleaned_data[self.key_value_fields[field]]
            mapping[key] = value
            key_store.data = mapping
            key_store.save()


class DefaultValidationForm(forms.Form):
    #Dynamic Form that creates validation fields based on given set of rules

    def __init__(self, *args, **kwargs):
        self.warnings = []
        self.rules = kwargs.pop('rules')
        self.file = kwargs.pop('file')
        self.key_value_fields = {}

        super(DefaultValidationForm, self).__init__(*args, **kwargs)

        for field in self.rules:
            if field['field_type'] == 'text':
                self.fields[field['field_name']] = forms.CharField(required=field['required'])
            elif field['field_type'] == 'integer':
                self.fields[field['field_name']] = forms.IntegerField(required=field['required'])
            elif field['field_type'] == 'decimal' or field['field_type'] == 'numeric':
                self.fields[field['field_name']] = forms.DecimalField(required=field['required'])
            elif field['field_type'] == 'date':
                input_formats = ['%Y%m%d', '%Y-%m-%d', '%Y/%m/%d']
                self.fields[field['field_name']] = CleanDateField(required=field['required'], input_formats=input_formats)
            elif field['field_type'] == 'boolean':
                self.fields[field['field_name']] = forms.BooleanField(required=field['required'])
            elif field['field_type'] == 'scientific_name':
                self.fields[field['field_name']] = ScientificNameField(required=field['required'])
            elif field['field_type'] == 'model':
                app = field['app']
                model = field['model']
                query_field = field['query_field']
                self.fields[field['field_name']] = ModelField(required=field['required'],
                    model=model, app=app, query_field=query_field)
            elif field['field_type'] == 'key_value':
                self.fields[field['field_name']] = forms.CharField(required=field['required'])
                self.key_value_fields[field] = field['value_field']
            elif field['field_type'] == 'key_look_up':
                etlfile = self.etlfile
                self.fields[field['field_name']] = KeyLookUpField(
                    required=field['required'],
                    etlfile=self.etlfile,
                    sheet_name=field['sheet_name'],
                    code=field['code'])
            else:
                print('Missing field_type', field)
                self.fields[field['field_name']] = forms.CharField(required=field['required'])

    def clean(self):
        cleaned_data = super(DefaultValidationForm, self).clean()
        return cleaned_data

    def save(self, sheet_name, row_index):
        cleaned_data = self.cleaned_data
        return cleaned_data