# Generated by Django 4.0.5 on 2022-10-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coredb', '0005_beachprofilesurvey'),
    ]

    operations = [
        migrations.AddField(
            model_name='beachprofilesurvey',
            name='description_of_fixed_point',
            field=models.TextField(default='non'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='beachprofilesurvey',
            name='team_leader_affiliation',
            field=models.CharField(default='non', max_length=200),
            preserve_default=False,
        ),
    ]