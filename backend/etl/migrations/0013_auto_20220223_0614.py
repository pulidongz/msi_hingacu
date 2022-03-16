# Generated by Django 3.2.5 on 2022-02-22 22:14

from django.db import migrations, models
import etl.models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0012_auto_20220223_0408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataextractionconfiguration',
            name='scope',
        ),
        migrations.AlterField(
            model_name='dataextractionconfiguration',
            name='extraction_type',
            field=models.CharField(choices=[('form', 'Form'), ('table_rows', 'Table Rows'), ('table_columns', 'Table Columns')], default='form', max_length=20),
        ),
        migrations.AlterField(
            model_name='dataextractionconfiguration',
            name='rules',
            field=models.JSONField(default=etl.models.default_rules),
        ),
    ]