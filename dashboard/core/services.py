import json
from urllib.error import HTTPError
import requests

class AccidentsService:
    def __init__(self, year):
        self.year = year

    def accidents(self):
        url = f"https://services1.arcgis.com/FZVaYraI7sEGQ6rF/arcgis/rest/services/movilidad_gdb/FeatureServer/{self.year}/query?outFields=*&where=1%3D1&f=geojson"
        try:
            response = requests.get(url=url)
            for i in range(10):
                data = [dict(zip(['radicado'], [response.json()['features'][i]['properties']['RADICADO']])) for i in range(0, 10)]

        except requests.exceptions.RequestException as err:
            return 0
        return data
