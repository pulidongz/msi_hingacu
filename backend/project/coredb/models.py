from django.contrib.gis.db import models
from etl.models import Workbook


class TimeStampModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Location(TimeStampModel):
    site_name = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    region = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, default="Philippines")

    def __str__(self):
        return f"{self.site_name.capitalize()}, {self.barangay.capitalize()}, {self.town.capitalize()}, {self.province.capitalize()}"

class ALWANStation(TimeStampModel):
    #The default spatial reference system for geometry fields is WGS84 (meaning the SRID is 4326)
    #https://docs.djangoproject.com/en/3.2/ref/contrib/gis/tutorial/

    MANAGEMENT_CHOICES = (
        ('None', 'None'),
        ('Locally Managed MPA', 'Locally Managed MPA'),
        ('Nationally Managed MPA', 'Nationally Managed MPA')
    )

    name = models.CharField(max_length=200)
    corner_1 = models.PointField()
    corner_2 = models.PointField()
    gps_datum = models.CharField(verbose_name="GPS Datum", max_length=200, default="WGS84")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    additional_information = models.TextField(blank=True, null=True)
    type_of_management = models.CharField(max_length=200, choices=MANAGEMENT_CHOICES)

    class Meta:
        verbose_name = "ALWAN Survey Station"
        verbose_name_plural = "ALWAN Survey Stations"

    def __str__(self):
        return f"{self.name}: {self.corner_1.coords}, {self.corner_2.coords}"

    @property
    def code(self):
        return f"STATION-{self.pk}: {self.name}"

    @property
    def corner_1_lat(self):
        return self.corner_1.coords[1]

    @property
    def corner_1_lon(self):
        return self.corner_1.coords[0]

    @property
    def corner_2_lat(self):
        return self.corner_2.coords[1]

    @property
    def corner_2_lon(self):
        return self.corner_2.coords[0]


class ALWANSurvey(TimeStampModel):
    database_number = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    station = models.ForeignKey(ALWANStation, on_delete=models.SET_NULL, null=True)
    team_leader_name = models.CharField(max_length=200)
    team_leader_contact_number = models.CharField(max_length=200)
    team_scientist_name = models.CharField(max_length=200)
    volunteer_1 = models.CharField(max_length=200)
    volunteer_2 = models.CharField(max_length=200)
    volunteer_3 = models.CharField(max_length=200)
    volunteer_4 = models.CharField(max_length=200, null=True, blank=True)
    volunteer_5 = models.CharField(max_length=200, null=True, blank=True)
    volunteer_6 = models.CharField(max_length=200, null=True, blank=True)
    workbook = models.ForeignKey(Workbook, on_delete=models.SET_NULL, null=True)
    curated = models.BooleanField(default=False)

    class Meta:
        verbose_name = "ALWAN Survey"
        verbose_name_plural = "ALWAN Surveys"

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


class BFFVolunteerCount(TimeStampModel):
    VOLUNTEER_CHOICES = (
        (1, "Volunteer 1"),
        (2, "Volunteer 2"),
        (3, "Volunteer 3"),
        (4, "Volunteer 4"),
        (5, "Volunteer 5"),
        (6, "Volunteer 6"),
    )

    survey = models.ForeignKey(ALWANSurvey, on_delete=models.CASCADE)
    volunteer = models.IntegerField(choices=VOLUNTEER_CHOICES)
    species_name = models.CharField(max_length=200)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.survey.code}: {self.species_name} COUNT"

"""
class TMICount(TimeStampModel):
    survey = models.ForeignKey(ALWANSurvey, on_delete=models.CASCADE)
    volunteer = models.CharField(max_length=200)
    species_name = models.CharField(max_length=200)
    count = models.IntegerField()

    class Meta:
        verbose_name = "Invertebrate Count"
        verbose_name_plural = "Invertebrate Counts"

    def __str__(self):
        return f"{self.survey.code}: {self.species_name} COUNT"


class Photoquadrat(TimeStampModel):
    survey = models.ForeignKey(ALWANSurvey, on_delete=models.CASCADE)
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
"""

class BeachProfileSurvey(TimeStampModel):
    transect_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    transect_orientation = models.CharField(max_length=200)
    description_of_fixed_point = models.TextField()
    time_at_waterline = models.TimeField()
    point_at_waterline = models.IntegerField()
    #tide_level = models.DecimalField(max_digits=10, decimal_places=3)
    #mtl = models.DecimalField(max_digits=10, decimal_places=3)
    start_point = models.PointField()
    end_point = models.PointField()
    team_leader_name = models.CharField(max_length=200)
    team_leader_contact_number = models.CharField(max_length=200)
    team_leader_affiliation = models.CharField(max_length=200)

    workbook = models.ForeignKey(Workbook, on_delete=models.SET_NULL, null=True)
    curated = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Beach Profile Surveys"
        verbose_name = "Beach Profile Survey"

    @property
    def corner_1_lat(self):
        return self.start_point.coords[1]

    @property
    def corner_1_lon(self):
        return self.start_point.coords[0]

    @property
    def corner_2_lat(self):
        return self.end_point.coords[1]

    @property
    def corner_2_lon(self):
        return self.end_point.coords[0]


"""
class CoastWalkSurvey(TimeStampModel):
    # when
    date = models.DateField()
    # where
    gps_datum = models.CharField(verbose_name="GPS Datum", max_length=200, default="WGS84")
    gps_unit = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    ## SHP FILE
    # who
    leader = models.CharField(max_length=200)
    leader_affiliation = models.CharField(max_length=200)
    leader_contact = models.CharField(max_length=200, null=True, blank=True)
    leader_email = models.EmailField(null=True, blank=True)
    # extra
    curated = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Coast Walk Surveys"
        verbose_name = "Coast Walk Survey"


class CoastalCompartmentData(TimeStampModel):
    survey = models.ForeignKey(CoastWalkSurvey, on_delete=models.SET_NULL, null=True)
    coastal_compartment = models.CharField(max_length=200)


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
"""