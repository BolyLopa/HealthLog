# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: HealthLog
import unittest
from datetime import date, timedelta

class TestHealthLogHelpers(unittest.TestCase):
    def test_validate_date_format(self):
        self.assertTrue(_is_valid_date("2023-10-27"))
        self.assertFalse(_is_valid_date("2023/10/27"))
        self.assertFalse(_is_valid_date("invalid"))

    def test_calculate_week_number(self):
        d = date(2023, 10, 27)
        week_num = _get_week_number(d)
        expected = (d - timedelta(days=d.weekday())).isoformat()[:4] + "-W" + str((d - timedelta(days=d.weekday()) + timedelta(days=days_in_week)).isocalendar()[1])
        self.assertEqual(week_num, f"{expected}")

    def test_create_entry_success(self):
        entry = _create_health_entry("weight", 70.5)
        self.assertIsNotNone(entry['id'])
        self.assertEqual(entry['type'], "measurement")
        self.assertAlmostEqual(entry['value'], 70.5, places=1)

if __name__ == '__main__':
    unittest.main()
