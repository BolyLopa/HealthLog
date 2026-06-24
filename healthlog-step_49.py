# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: HealthLog
import unittest
from healthlog import HealthLog, Habit, Measurement, Symptom

class TestHealthLogEdgeCases(unittest.TestCase):
    def setUp(self):
        self.log = HealthLog()
    
    def test_delete_nonexistent_entry(self):
        with self.assertRaises(ValueError) as context:
            self.log.delete("non_existent_id")
        self.assertIn("not found", str(context.exception))

    def test_update_with_invalid_date(self):
        habit = Habit(name="Drink Water", frequency=1, unit="ml", target=2000)
        self.log.add(habit)
        with self.assertRaises(ValueError) as context:
            self.log.update("habit_0", {"date": "invalid-date"})
        self.assertIn("invalid date format", str(context.exception))

    def test_update_missing_id(self):
        with self.assertRaises(ValueError) as context:
            self.log.update(None, {})
        self.assertIn("entry not found", str(context.exception))

    def test_delete_last_measurement_of_habit(self):
        habit = Habit(name="Drink Water", frequency=1, unit="ml", target=2000)
        m1 = Measurement(habit_id="habit_0", value=500, date="2023-01-01")
        self.log.add(m1)
        self.log.delete("measurement_0")
        entries = list(self.log.get_entries())
        self.assertEqual(len(entries), 0)

    def test_update_symptom_with_invalid_severity(self):
        symptom = Symptom(name="Headache", severity=5, date="2023-01-01")
        self.log.add(symptom)
        with self.assertRaises(ValueError) as context:
            self.log.update("symptom_0", {"severity": 6})
        self.assertIn("invalid severity", str(context.exception))

if __name__ == "__main__":
    unittest.main()
