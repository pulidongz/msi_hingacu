from django import forms
from curation.models import Curation


class CurationForm(forms.ModelForm):
    class Meta:
        model = Curation
        fields = ['workbook', 'verdict', 'reason']
