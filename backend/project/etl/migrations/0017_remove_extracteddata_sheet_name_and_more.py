# Generated by Django 4.0.5 on 2022-06-17 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0016_remove_extracteddata_etlfile_extracteddata_workbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracteddata',
            name='sheet_name',
        ),
        migrations.RemoveField(
            model_name='extracteddata',
            name='sheet_slug',
        ),
        migrations.RemoveField(
            model_name='extracteddata',
            name='warnings',
        ),
        migrations.AddField(
            model_name='extracteddata',
            name='configuration',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='etl.dataextractionconfiguration'),
            preserve_default=False,
        ),
    ]
