import env
from fake_external_services.fake_services import national_identification_service_mock, national_archive


URL_DIRECTORY = {
    f'{env.NATIONAL_IDENTIFICATION_SERVICE_URL}{env.GET_IDENTIFICATION}': national_identification_service_mock,
    f'{env.NATIONAL_IDENTIFICATION_SERVICE_URL}{env.GET_JUDICIAL_RECORDS}': national_archive
}