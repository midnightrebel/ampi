import requests

from nasa.apps.models import Coordinates


def get_info_from_api(name):
    if name == 'FALCONSAT':
        url = 'https://tle.ivanstanojevic.me/api/tle/30776'
    if name == 'AISSAT':
        url = 'https://tle.ivanstanojevic.me/api/tle/40075'
    if name == 'PROXIMA':
        url = 'https://tle.ivanstanojevic.me/api/tle/43694'
    response = requests.get(url).json()
    return response

def save_info_to_db(info):
    Coordinates.objects.create(
        name=info['name'],
        satelliteId=info['satelliteId'],
        date=info['date'],
        line1=info['line1'],
        line2=info['line2'],
    )

def get_info_to_db():
    qs = Coordinates.objects.all()
    return qs