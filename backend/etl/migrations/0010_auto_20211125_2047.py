# Generated by Django 3.2.5 on 2021-11-25 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('etl', '0009_auto_20211025_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='extracteddata',
            options={'verbose_name': 'Extracted Data', 'verbose_name_plural': 'Extracted Data'},
        ),
        migrations.AlterField(
            model_name='dcpcollection',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extracteddata',
            name='etlfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='etl.etlfile', verbose_name='ETL File'),
        ),
    ]
