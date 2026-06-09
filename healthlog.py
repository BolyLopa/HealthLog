# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: HealthLog
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

class HealthLog:
    def __init__(self):
        self.entries: List[Dict[str, Any]] = []
        self.habits: Dict[str, str] = {}
        self.measurements: Dict[str, float] = {}
        self.symptoms: Dict[str, List[str]] = {}

    def add_entry(self, date: datetime, habit: Optional[str], 
                  measurement: Optional[tuple[str, float]], symptom: Optional[str]):
        entry = {
            "date": date.strftime("%Y-%m-%d"),
            "habit": habit,
            "measurement": measurement,
            "symptom": symptom
        }
        self.entries.append(entry)
        if habit: self.habits[habit] = True
        if measurement: 
            key = f"{measurement[0]}_{measurement[1]}"
            self.measurements[key] = self.measurements.get(key, 0) + 1
        if symptom:
            if symptom not in self.symptoms: self.symptoms[symptom] = []
            self.symptoms[symptom].append(entry["date"])

    def get_weekly_summary(self, start_date: datetime) -> Dict[str, Any]:
        end_date = start_date + timedelta(days=7)
        week_entries = [e for e in self.entries if start_date <= datetime.strptime(e["date"], "%Y-%m-%d") < end_date]
        return {
            "start": start_date.strftime("%Y-%m-%d"),
            "end": end_date.strftime("%Y-%m-%d"),
            "count": len(week_entries),
            "habits_done": list(set(e["habit"] for e in week_entries if e["habit"])),
            "symptoms_reported": list(set(e["symptom"] for e in week_entries if e["symptom"]))
        }

# Demo dataset initialization
demo_data = [
    ("2023-10-01", "Morning Run", ("weight", 75.5), None),
    ("2023-10-02", "Yoga", ("blood_pressure", 120/80), "Headache"),
    ("2023-10-03", "Morning Run", ("weight", 75.4), None),
    ("2023-10-04", "Reading", None, "Fatigue"),
    ("2023-10-05", "Morning Run", ("weight", 75.3), None),
]

log = HealthLog()
for date_str, habit, meas, symp in demo_data:
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    log.add_entry(dt, habit, meas, symp)

print(json.dumps(log.get_weekly_summary(datetime.strptime("2023-10-01", "%Y-%m-%d")), indent=2))
