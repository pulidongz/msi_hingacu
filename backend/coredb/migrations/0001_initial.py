# Generated by Django 3.2.5 on 2021-07-04 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coastal_stability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('monitoring_site', models.CharField(blank=True, max_length=250, null=True)),
                ('survey_length', models.CharField(blank=True, max_length=250, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('poster', models.CharField(blank=True, max_length=250, null=True)),
                ('survey_remarks', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='connectivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='coral_deep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('depth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('live_coral', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('sand_rubble', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('dead_coral', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('other', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('species_richness', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='coral_shallow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fish_biology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('benthic_invertivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('corallivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('detritivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('herbivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('omnivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('piscivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('planktivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fish_density',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('benthic_invertivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('corallivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('detritivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('herbivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('omnivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('piscivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('planktivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fish_species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('benthic_invertivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('corallivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('detritivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('herbivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('omnivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('piscivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
                ('planktivore', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mangrove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('present_extent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('historical_extent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mangrove_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='seagrass_cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='seagrass_density',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField(blank=True, default=0, null=True)),
                ('survey_date', models.DateTimeField(blank=True, null=True)),
                ('present_extent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('historical_extent', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
