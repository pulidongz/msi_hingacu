# Generated by Django 4.0.5 on 2022-10-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0028_workbook_attachments_alter_workbook_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataextractionconfiguration',
            options={'verbose_name': 'Worksheet Section', 'verbose_name_plural': 'Worksheet Sections'},
        ),
        migrations.AddField(
            model_name='workbookconfiguration',
            name='publisher_class',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='datafield',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('decimal', 'Decimal'), ('date', 'Date'), ('time', 'Time'), ('boolean', 'Boolean'), ('coordinate', 'Coordinate')], default='text', max_length=20),
        ),
    ]
