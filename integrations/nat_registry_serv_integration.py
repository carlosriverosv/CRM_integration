import env
from fake_external_services import requests

async def check_person_exists(person_national_id):
    url = f'''{env.NATIONAL_IDENTIFICATION_SERVICE_URL}{env.NATIONAL_IDENTIFICATION_SERVICES['get_identification']}{person_national_id}'''
    return await requests.get(url)
