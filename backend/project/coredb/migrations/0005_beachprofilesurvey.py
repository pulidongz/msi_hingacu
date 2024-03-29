# Generated by Django 4.0.5 on 2022-10-24 16:39

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0030_workbookconfiguration_component'),
        ('coredb', '0004_alwansurvey_database_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeachProfileSurvey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('transect_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('transect_orientation', models.CharField(max_length=200)),
                ('time_at_waterline', models.TimeField()),
                ('point_at_waterline', models.IntegerField()),
                ('tide_level', models.DecimalField(decimal_places=3, max_digits=10)),
                ('mtl', models.DecimalField(decimal_places=3, max_digits=10)),
                ('start_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('end_point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('team_leader_name', models.CharField(max_length=200)),
                ('team_leader_contact_number', models.CharField(max_length=200)),
                ('curated', models.BooleanField(default=False)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coredb.location')),
                ('workbook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='etl.workbook')),
            ],
            options={
                'verbose_name': 'Beach Profile Survey',
                'verbose_name_plural': 'Beach Profile Surveys',
            },
        ),
    ]
