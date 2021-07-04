from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(coastal_stability)
class coastal_stability_admin(admin.ModelAdmin):
	list_display = ("location_id", "monitoring_site", "survey_length","survey_date", "poster", "survey_remarks")
	list_filter = ("monitoring_site",)
	search_fields = ("monitoring_site", )

@admin.register(connectivity)
class connectivity_admin(admin.ModelAdmin):
    pass

@admin.register(coral_deep)
class coral_deep_admin(admin.ModelAdmin):
    pass

@admin.register(coral_shallow)
class coral_shallow_admin(admin.ModelAdmin):
    pass

@admin.register(fish_biology)
class fish_biology_admin(admin.ModelAdmin):
    pass

@admin.register(fish_density)
class fish_density_admin(admin.ModelAdmin):
    pass

@admin.register(fish_species)
class fish_species_admin(admin.ModelAdmin):
    pass

@admin.register(mangrove)
class mangrove_admin(admin.ModelAdmin):
    pass

@admin.register(mangrove_data)
class mangrove_data_admin(admin.ModelAdmin):
    pass

@admin.register(seagrass_cover)
class seagrass_cover_admin(admin.ModelAdmin):
    pass

@admin.register(seagrass_density)
class seagrass_density_admin(admin.ModelAdmin):
    pass

