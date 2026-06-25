# === Stage 51: Add unit tests for search and filter behavior ===
# Project: HealthLog
import unittest
from healthlog import HealthLog, EntryType

class TestHealthLogSearch(unittest.TestCase):
    def setUp(self):
        self.log = HealthLog()
    
    def test_search_by_keyword_in_text(self):
        entry1 = self.log.add_entry(EntryType.SYMPTOM, "Headache", text="Mild headache after coffee")
        entry2 = self.log.add_entry(EntryType.HABIT, "Drink Water", text="Drank 500ml water")
        results = self.log.search("headache")
        self.assertEqual(len(results), 1)
        self.assertIn(entry1.id, [e.id for e in results])

    def test_filter_by_date_range(self):
        entry1 = self.log.add_entry(EntryType.MEASUREMENT, "Weight", value=70.5, date="2023-10-01")
        entry2 = self.log.add_entry(EntryType.MEASUREMENT, "Weight", value=71.0, date="2023-10-08")
        results = self.log.filter_by_date("2023-10-05", "2023-10-06")
        self.assertEqual(len(results), 0)

    def test_filter_by_type(self):
        entry1 = self.log.add_entry(EntryType.HABIT, "Sleep", text="8 hours")
        results = self.log.filter_by_type(EntryType.SYMPTOM)
        self.assertEqual(len(results), 0)
