import json
from random import random, randrange
import time
import asyncio

async def introduce_delay():
    delay_time = randrange(1, 10)
    await asyncio.sleep(delay_time)
    return delay_time

async def national_identification_service_mock(person_national_id):
    delay_time = await introduce_delay()
    return json.dumps({
        'status_code': 200,
        'response': random() < 0.9,
        'sleep': delay_time,
        })

async def national_archive(person_national_id):
    delay_time = await introduce_delay()
    return json.dumps({
        'status_code': 200,
        'response': random() > 0.8,
        'sleep': delay_time,
        })