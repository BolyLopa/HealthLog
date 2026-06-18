# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: HealthLog
from datetime import datetime, timedelta
def get_upcoming_reminders(habits: list[dict], symptoms: list[dict]) -> list[str]:
    now = datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    reminders = []
    for habit in habits:
        if habit.get("enabled", True) and habit.get("frequency", "daily"):
            next_date = (now + timedelta(days=1)).strftime("%Y-%m-%d")
            reminders.append(f"[Habit] {habit['name']} scheduled for {next_date}")
    for symptom in symptoms:
        if symptom.get("enabled", True) and symptom.get("frequency", "weekly"):
            next_week = (now + timedelta(weeks=1)).strftime("%Y-%m-%d")
            reminders.append(f"[Symptom] Log check-up scheduled for {next_week}")
    return reminders
