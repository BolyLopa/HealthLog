# === Stage 36: Add templates for quickly creating common records ===
# Project: HealthLog
from datetime import date, timedelta
import random

def create_daily_record():
    """Generates a template for a single day's log entry."""
    return {
        "date": str(date.today()),
        "habits": {"water_ml": 0, "exercise_min": 0, "sleep_hours": 8},
        "measurements": {"weight_kg": None, "blood_pressure": None},
        "symptoms": [],
        "notes": ""
    }

def create_weekly_summary():
    """Generates a template for a weekly summary report."""
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    return {
        "week_start": week_start,
        "total_habit_completion_rate": 0.0,
        "avg_sleep_hours": 0.0,
        "symptoms_encountered": [],
        "weekly_notes": ""
    }

def create_symptom_entry(symptom_name: str):
    """Generates a template for logging a specific symptom."""
    return {
        "timestamp": date.today().isoformat(),
        "name": symptom_name,
        "severity": random.choice(["mild", "moderate", "severe"]),
        "description": "",
        "resolved": False
    }

def create_measurement_entry(measurement_type: str):
    """Generates a template for logging a physical measurement."""
    return {
        "timestamp": date.today().isoformat(),
        "type": measurement_type,
        "value": None,
        "unit": "",
        "notes": ""
    }
