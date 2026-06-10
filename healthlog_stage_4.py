# === Stage 4: Implement create operations for the primary records ===
# Project: HealthLog
from datetime import datetime, timedelta
import os

def create_habit_entry(habit_name: str, date: datetime = None):
    if date is None:
        date = datetime.now()
    filename = f"habits/{habit_name}_{date.strftime('%Y-%m-%d')}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Habit: {habit_name}\nDate: {date.strftime('%Y-%m-%d %H:%M:%S')}\nStatus: Completed\n")

def create_measurement_entry(measurement_type: str, value: float, unit: str, date: datetime = None):
    if date is None:
        date = datetime.now()
    filename = f"measurements/{measurement_type}_{date.strftime('%Y-%m-%d')}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Type: {measurement_type}\nValue: {value}\nUnit: {unit}\nDate: {date.strftime('%Y-%m-%d %H:%M:%S')}\n")

def create_symptom_entry(symptom_name: str, description: str, severity: int = 1, date: datetime = None):
    if date is None:
        date = datetime.now()
    filename = f"symptoms/{symptom_name}_{date.strftime('%Y-%m-%d')}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Symptom: {symptom_name}\nDescription: {description}\nSeverity: {severity}/10\nDate: {date.strftime('%Y-%m-%d %H:%M:%S')}\n")

def create_weekly_summary(start_date: datetime, end_date: datetime):
    if start_date > end_date:
        raise ValueError("Start date must be before end date")
    summary_file = f"summaries/weekly_{start_date.strftime('%Y-%m-%d')}_{end_date.strftime('%Y-%m-%d')}.txt"
    os.makedirs(os.path.dirname(summary_file), exist_ok=True)
    
    # Placeholder logic for summary generation
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"Weekly Summary\nStart: {start_date.strftime('%Y-%m-%d')}\nEnd: {end_date.strftime('%Y-%m-%d')}\n")
        f.write("Notes: Review completed habits and average measurements.\n")
