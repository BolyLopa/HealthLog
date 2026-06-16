# === Stage 25: Add daily summary calculations ===
# Project: HealthLog
def calculate_daily_summary(day_data):
    habits = day_data.get("habits", {})
    measurements = day_data.get("measurements", [])
    symptoms = day_data.get("symptoms", [])
    
    completed_habits = sum(1 for h in habits.values() if h.get("completed"))
    total_measurements = len(measurements)
    avg_sleep = None
    avg_heart_rate = None
    
    sleep_entries = [m["value"] for m in measurements if m.get("type") == "sleep_hours"]
    hr_entries = [m["value"] for m in measurements if m.get("type") == "heart_rate_bpm"]
    
    if sleep_entries:
        avg_sleep = sum(sleep_entries) / len(sleep_entries)
    if hr_entries:
        avg_heart_rate = sum(hr_entries) / len(hr_entries)
    
    symptom_count = len(symptoms)
    summary_text = f"Completed {completed_habits}/{len(habits)} habits. "
    summary_text += f"Avg sleep: {avg_sleep:.1f}h, Avg HR: {avg_heart_rate:.0f}bpm. "
    summary_text += f"Symptoms reported: {symptom_count}"
    
    return {
        "completed_habits": completed_habits,
        "total_measurements": total_measurements,
        "avg_sleep_hours": avg_sleep,
        "avg_heart_rate_bpm": avg_heart_rate,
        "symptom_count": symptom_count,
        "summary_text": summary_text
    }
