from projects import constants
from projects.models import Staff
from etl.models import ETLFile
from etl.utils import convert_to_datetime


def process_staff(etlfile):
    etl_file = ETLFileHandler(etlfile)
    key_map = { # column name to field mapping
        'project': 'project type',
        'name': 'contact person',
        'code': 'code',
        'position': 'assignment',
        'contact_number': 'tel #',
        'email': 'email',
        'point_person': 'point person',
        'contract_end': 'contract expiry'
    }
    data = etl_file.get_data(key_map)
    
    for person in data:
        print(person)
        staff, created = Staff.objects.get_or_create(
            code=person['code'],
            defaults={
                'name': person['name'],
                'project': person['project'],
                'position': person['position'],
                'contact_number': person['contact_number'],
                'email': person['email'],
                'point_person': bool(person['point_person']),
                'contract_end': convert_to_datetime(person['contract_end'])
            },
        )
