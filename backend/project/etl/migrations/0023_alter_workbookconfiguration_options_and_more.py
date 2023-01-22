# Generated by Django 4.0.5 on 2022-08-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0022_dataextractionconfiguration_scope_datafield_cell'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workbookconfiguration',
            options={'ordering': ['name'], 'verbose_name': 'Workbook Layout', 'verbose_name_plural': 'Workbook Layouts'},
        ),
        migrations.RemoveField(
            model_name='dataextractionconfiguration',
            name='scope',
        ),
        migrations.AddField(
            model_name='dataextractionconfiguration',
            name='max_col',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='dataextractionconfiguration',
            name='max_row',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='dataextractionconfiguration',
            name='min_col',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dataextractionconfiguration',
            name='min_row',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='datafield',
            name='field_index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datafield',
            name='field_type',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('decimal', 'Decimal'), ('date', 'Date'), ('time', 'Time'), ('boolean', 'Boolean')], default='text', max_length=20),
        ),
    ]