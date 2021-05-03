import unittest
from internal_prospect_qual import internal_qualification

class InternalProspectTest(unittest.TestCase):

    def test_internal_qualification_not_person_judicial_records(self):
        self.assertEqual(internal_qualification(False, True), 0)

    def test_internal_qualification_person_with_judicial_records(self):
        self.assertEqual(internal_qualification(True, True), 0)

    def test_internal_qualification_person_no_judicial_records(self):
        self.assertNotEqual(internal_qualification(True, False), 0)

    def test_internal_qualification_not_person_no_judicial_records(self):
        self.assertEqual(internal_qualification(False, False), 0)
