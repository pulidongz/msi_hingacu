from django.db import models

# Create your models here.
class coastal_stability(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    monitoring_site = models.CharField(max_length=250, null=True, blank=True)
    survey_length = models.CharField(max_length=250, null=True, blank=True)
    survey_date = models.DateTimeField(blank=True, null=True)
    poster = models.CharField(max_length=250, null=True, blank=True)
    survey_remarks = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Coastal Stability"

class connectivity(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    date = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Connectivity"

class coral_deep(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    depth = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    live_coral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    sand_rubble = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    dead_coral = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    other = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    species_richness = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    remarks = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Deep Coral"

class coral_shallow(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Shallow Coral"

class fish_biology(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    benthic_invertivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    corallivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    detritivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    herbivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    omnivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    piscivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    planktivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Fish Biology"

class fish_density(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    benthic_invertivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    corallivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    detritivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    herbivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    omnivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    piscivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    planktivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Fish Density"

class fish_species(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    benthic_invertivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    corallivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    detritivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    herbivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    omnivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    piscivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)
    planktivore = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Fish Species"

class mangrove(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    present_extent = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    historical_extent = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    remarks = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Mangrove"

class mangrove_data(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Mangrove Data"

class seagrass_cover(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Seagrass Cover"

class seagrass_density(models.Model):
    location_id = models.IntegerField(null=True, blank=True, default=0)
    survey_date = models.DateTimeField(blank=True, null=True)
    present_extent = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    historical_extent = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True, default=0)
    remarks = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Seagrass Density"