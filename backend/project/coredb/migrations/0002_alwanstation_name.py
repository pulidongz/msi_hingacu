# Generated by Django 4.0.5 on 2022-10-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coredb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alwanstation',
            name='name',
            field=models.CharField(default='STATION NAME', max_length=200),
            preserve_default=False,
        ),
    ]