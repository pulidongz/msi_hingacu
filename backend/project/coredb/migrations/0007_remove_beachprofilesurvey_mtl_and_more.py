# Generated by Django 4.0.5 on 2022-10-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coredb', '0006_beachprofilesurvey_description_of_fixed_point_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beachprofilesurvey',
            name='mtl',
        ),
        migrations.RemoveField(
            model_name='beachprofilesurvey',
            name='tide_level',
        ),
    ]
