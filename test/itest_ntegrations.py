import unittest
import json
import asyncio
from integrations.nat_registry_serv_integration import check_person_exists
from integrations.nat_archive_serv_integration import check_judicial_records
from internal_process.prospect_process import could_turn_into_prospect
from unittest.mock import patch


@patch('integrations.nat_archive_serv_integration.check_judicial_records')
async def check_judicial_records(person_id, mock_f):
    return json.dumps({
        'status_code': 200,
        'response': person_id == 2,
        'sleep': 5,
    })

@patch('integrations.nat_registry_serv_integration.check_person_exists')
async def check_person_exists(person_id, mock_f):
    return json.dumps({
        'status_code': 200,
        'response': True,
        'sleep': 5,
    })

class IntegrationsTest(unittest.IsolatedAsyncioTestCase):

    async def test_nat_registry_serv(self):
        response =  await check_person_exists(2)
        response_json = json.loads(response)
        self.assertEqual(response_json['status_code'], 200)
        self.assertTrue(response_json['response'])

    async def test_nat_archive_serv(self):
        response = await check_judicial_records(2)
        response_json = json.loads(response)
        print(response_json)
        self.assertEqual(response_json['status_code'], 200)
        self.assertFalse(response_json['response'])
    

    async def test_turn_into_prospect_yes(self):
        qualification_result = await could_turn_into_prospect(5)
        self.assertGreaterEqual(qualification_result, 0)
        self.assertLessEqual(qualification_result, 100)

    async def test_turn_into_prospect_no(self):
        qualification_result = await could_turn_into_prospect(2)
        print(qualification_result)
        self.assertEqual(qualification_result, 0)