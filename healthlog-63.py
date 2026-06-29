# === Stage 63: Add relationships between records where useful ===
# Project: HealthLog
from datetime import date, timedelta
from typing import Optional, List
import json

class HealthRecord:
    def __init__(self, record_type: str, value: float | None = None, notes: str = ""):
        self.id = id(self)
        self.type = record_type  # 'habit', 'measurement', 'symptom'
        self.value = value
        self.notes = notes
        self.date = date.today()
        self.related_records: List['HealthRecord'] = []

    def add_related(self, other: 'HealthRecord'):
        if other not in self.related_records and other.id != self.id:
            self.related_records.append(other)
            other.related_records.append(self)

class HealthLog:
    def __init__(self):
        self.records: List[HealthRecord] = []
        self.weekly_summaries: dict[date, str] = {}

    def add_record(self, record_type: str, value: float | None = None, notes: str = "") -> HealthRecord:
        rec = HealthRecord(record_type, value, notes)
        self.records.append(rec)
        return rec

    def generate_weekly_summary(self):
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        
        current_week_records = [r for r in self.records if week_start <= r.date <= week_end]
        
        habit_count = sum(1 for r in current_week_records if r.type == 'habit' and r.value is not None)
        measurement_avg = sum(r.value for r in current_week_records if r.type == 'measurement') / max(sum(1 for r in current_week_records if r.type == 'measurement'), 1)
        symptom_count = sum(1 for r in current_week_records if r.type == 'symptom' and r.notes != "")

        summary_text = f"Week of {week_start} to {week_end}: "
        summary_text += f"Habits completed: {habit_count}, "
        summary_text += f"Average measurement: {measurement_avg:.1f}, "
        summary_text += f"Symptoms noted: {symptom_count}"

        self.weekly_summaries[week_start] = summary_text
