from coredb.models import ALWANStation, ALWANSurvey, Photoquadrat, PhotoquadratPoint
from ddf import G

def create_dummies():
    # create a station and two surveys per station
    for i in range(0, 2):
        station = G(ALWANStation)
        for j in range(0, 2):
            survey = G(ALWANSurvey, station=station)
            for k in range(0, 10):
                species = f"SPECIES {k}"
                for l in range(0, 4):
                    volunteer = f"VOLUNTEER {l}"
                    fish_count = G(FishCount, species_name=species, volunteer=volunteer, survey=survey)
                    invert_count = G(InvertebrateCount, species_name=species, volunteer=volunteer, survey=survey)
            for m in range(0, 5):
                image = f"IMAGE {m}"
                photoquadrat = G(Photoquadrat, image_label=image, file_name=image, survey=survey)
                for n in range(0, 10):
                    category = f"CATEGORY {n}"
                    photoquadrat_point = G(PhotoquadratPoint, photoquadrat=photoquadrat, major_category=category)