import asyncio
import time
import json
import logging
from integrations.nat_registry_serv_integration import check_person_exists
from integrations.nat_archive_serv_integration import check_judicial_records
from internal_process.internal_prospect_qual import internal_qualification
from utils.utils import convert_lead_into_prospect


logger = logging.getLogger(__name__)

async def could_turn_into_prospect(person_id):
    try:
        results = await asyncio.gather(check_person_exists(person_id),check_judicial_records(person_id))
        person_exist_result = json.loads(results[0])
        judicial_records_result = json.loads(results[1])
        if person_exist_result['status_code'] == 200 and judicial_records_result['status_code'] == 200:
            internal_qualification_result = internal_qualification(person_exist_result['response'], judicial_records_result['response'])
            return internal_qualification_result
    except Exception:
        logger.error('error running turn into prospect', extra={'person_id': person_id})


async def process_validation(persons_ids):
    print(f"started at {time.strftime('%X')}")
    results = await asyncio.gather(*[asyncio.create_task(could_turn_into_prospect(person_id)) for person_id in persons_ids])
    for person_id, internal_qualification_result in zip(persons_ids, results):
        convert_lead_into_prospect(person_id, internal_qualification_result)
    print(f"finished at {time.strftime('%X')}")