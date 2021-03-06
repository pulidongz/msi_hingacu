# Generated by Django 3.2.5 on 2021-10-25 02:56

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0008_auto_20210802_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacapturepoint',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='datacapturepoint',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dcpcollection',
            name='code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='ExtractedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('sheet_name', models.CharField(max_length=64)),
                ('sheet_slug', django_extensions.db.fields.AutoSlugField(allow_duplicates=True, blank=True, default=None, editable=False, null=True, populate_from='sheet_name')),
                ('data', models.JSONField()),
                ('warnings', models.JSONField(null=True)),
                ('etlfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.etlfile')),
            ],
            options={
                'verbose_name': 'Datasheet Field Data',
                'verbose_name_plural': 'Datasheet Field Data',
            },
        ),
    ]
