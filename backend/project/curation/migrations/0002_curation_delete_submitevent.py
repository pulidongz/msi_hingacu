# Generated by Django 4.0.5 on 2022-09-12 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0024_alter_workbookconfiguration_options_and_more'),
        ('curation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('verdict', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending Review')], default='pending', max_length=30)),
                ('reason', models.TextField()),
                ('verdict_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='curation.curator')),
                ('workbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.workbook')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='SubmitEvent',
        ),
    ]
