from random import randint

def internal_qualification(person_exists, judicial_records):
    if person_exists and not judicial_records:
        return randint(0, 100)
    return 0