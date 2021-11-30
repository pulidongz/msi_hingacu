from django.contrib.gis.db import models


class TimeStampModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Station(TimeStampModel):
    #The default spatial reference system for geometry fields is WGS84 (meaning the SRID is 4326)
    #https://docs.djangoproject.com/en/3.2/ref/contrib/gis/tutorial/

    MANAGEMENT_CHOICES = (
        ('None', 'None'),
        ('Locally Managed MPA', 'Locally Managed MPA'),
        ('Nationally Managed MPA', 'Nationally Managed MPA')
    )

    reef_name = models.CharField(max_length=200)
    start_point = models.PointField()
    end_point = models.PointField()
    gps_datum = models.CharField(verbose_name="GPS Datum", max_length=200, default="WGS84")
    barangay = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    type_of_management = models.CharField(max_length=200, choices=MANAGEMENT_CHOICES)
    additional_information = models.TextField(blank=True, null=True)
    curated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Survey Station"
        verbose_name_plural = "Survey Stations"
        unique_together = [['start_point', 'end_point']]

    def __str__(self):
        return f"{self.code}: {self.start_point.coords}, {self.end_point.coords}"

    @property
    def code(self):
        return f"STATION-{self.pk}"

    @property
    def start_point_lat(self):
        return self.start_point.y

    @property
    def start_point_lon(self):
        return self.start_point.x

    @property
    def end_point_lat(self):
        return self.end_point.y

    @property
    def end_point_lon(self):
        return self.end_point.x

    def get_survey_count(self, curated=None):
        if curated is not None:
            return self.al1survey_set.filter(curated=curated).count()
        return self.al1survey_set.all().count()



class AL1Survey(TimeStampModel):
    date = models.DateField()
    time = models.TimeField()
    station = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
    team_leader = models.CharField(max_length=200)
    team_scientist = models.CharField(max_length=200)
    curated = models.BooleanField(default=False)
    #VOLUNTEERS (Full names)
    #TEAM LEADER/TEAM SCIENTIST AFFILIATION and CONTACT DETAILS

    class Meta:
        verbose_name = "AL1 Survey"
        verbose_name_plural = "AL1 Surveys"

    def __str__(self):
        return f"{self.code}"

    @property
    def code(self):
        return f"AL1-{self.pk}"

    def generate_fish_report(self):
        species_dict = {}
        counts = self.fishcount_set.all()
        for c in counts:
            if not c.species_name in species_dict:
                species_dict[c.species_name] = {}
            species_dict[c.species_name][c.volunteer] = c.count
        for species in species_dict.keys():
            species_dict[species].update(counts.filter(species_name=species).aggregate(
                mean=models.Avg('count'),
                range=models.Max('count') - models.Min('count')))
        report = {
            'summary': {
                'species_richness': counts.aggregate(
                    mean=models.Avg('count'),
                    range=models.Max('count') - models.Min('count')),
            },
            'breakdown': species_dict.items(),
        }
        return report

    def generate_invertebrate_report(self):
        species_dict = {}
        counts = self.invertebratecount_set.all()
        for c in counts:
            if not c.species_name in species_dict:
                species_dict[c.species_name] = {}
            species_dict[c.species_name][c.volunteer] = c.count
        for species in species_dict.keys():
            species_dict[species].update(counts.filter(species_name=species).aggregate(
                mean=models.Avg('count'),
                range=models.Max('count') - models.Min('count')))
        report = {
            'summary': {
                'species_richness': counts.aggregate(
                    mean=models.Avg('count'),
                    range=models.Max('count') - models.Min('count')),
            },
            'breakdown': species_dict.items(),
        }
        return report


class FishCount(TimeStampModel):
    survey = models.ForeignKey(AL1Survey, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length=200)
    species_name = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        verbose_name = "Fish Count"
        verbose_name_plural = "Fish Counts"

    def __str__(self):
        return f"{self.survey.code}: {self.species_name} COUNT"


class InvertebrateCount(TimeStampModel):
    survey = models.ForeignKey(AL1Survey, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length=200)
    species_name = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        verbose_name = "Invertebrate Count"
        verbose_name_plural = "Invertebrate Counts"

    def __str__(self):
        return f"{self.survey.code}: {self.species_name} COUNT"


class Photoquadrat(TimeStampModel):
    survey = models.ForeignKey(AL1Survey, on_delete=models.CASCADE)
    image_label = models.CharField(max_length=200)
    file_name = models.CharField(max_length=200)
    remarks = models.TextField(blank=True, null=True)
    # reef state counts
    cot = models.IntegerField() # COT - crown of thorns count
    diseased = models.IntegerField() # Dis - diseased count
    bleached = models.IntegerField() # Blec - bleached count
    # human impact counts
    blast_fishing_craters = models.IntegerField()
    anchor_damage_craters = models.IntegerField()
    trash = models.IntegerField()

    class Meta:
        verbose_name = "Photoquadrat"
        verbose_name_plural = "Photoquadrats"

    def __str__(self):
        return f"{self.survey.code}: {self.file_name} QUADRAT {self.pk}"


class PhotoquadratPoint(TimeStampModel):
    photoquadrat = models.ForeignKey(Photoquadrat, on_delete=models.CASCADE)
    major_category = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Photoquadrat Point"
        verbose_name_plural = "Photoquadrats Points"

    def __str__(self):
        return f"QUADRAT {self.photoquadrat.pk}: POINT {self.pk}"


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
