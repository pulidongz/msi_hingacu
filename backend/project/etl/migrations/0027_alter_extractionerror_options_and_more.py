# Generated by Django 4.0.5 on 2022-10-12 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0026_remove_workbook_file_errors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extractionerror',
            options={'verbose_name': 'Extraction Error', 'verbose_name_plural': 'Extraction Errors'},
        ),
        migrations.AddField(
            model_name='extractionerror',
            name='entry_number',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='extractionerror',
            name='configuration',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='etl.dataextractionconfiguration'),
        ),
    ]
