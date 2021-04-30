import env
import re
import asyncio
from fake_external_services.exceptions import InvalidURL
from fake_external_services.mock_urls import URL_DIRECTORY

DOMAIN_REGEX = 'https://[a-z]*\.[a-z]{3}/[a-z]*/'


def get_person_id_and_url_path(url):
    try:
        domain = re.match(DOMAIN_REGEX, url).group(0)
        if not domain or not URL_DIRECTORY.get(domain):
            raise InvalidURL()
        person_id = url.split(domain)[1].split('/')[-1]
        try:
            return int(person_id), domain
        except ValueError:
            raise InvalidPersonIdURL()
    except IndexError:
        raise InvalidURL()
    

def get(url):
    person_id, domain = get_person_id_and_url_path(url)
    if not URL_DIRECTORY.get(domain):
        raise InvalidURL()
    return URL_DIRECTORY[domain](person_id)
