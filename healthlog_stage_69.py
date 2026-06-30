# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: HealthLog
def reset_demo_data():
    from datetime import date, timedelta
    today = date.today()
    
    # Clear all previous demo entries to ensure a clean state for testing
    with open("data.json", "w") as f:
        json.dump({
            "habits": {
                "water_intake": {"name": "Вода (мл)", "target": 2500, "unit": "ml"},
                "exercise_minutes": {"name": "Тренировка (мин)", "target": 30, "unit": "min"}
            },
            "measurements": {
                "weight_kg": {"name": "Вес", "unit": "kg"},
                "bpm_resting": {"name": "Пульс покоя", "unit": "уд/мин"}
            },
            "symptoms": [],
            "weekly_summary": {}
        }, f)

    # Populate with 7 days of realistic demo data for immediate testing
    entries = []
    for i in range(6, -1, -1):
        d = today - timedelta(days=i)
        entry_date = d.strftime("%Y-%m-%d")
        
        habit_data = {
            "water_intake": {"value": 2000 + (i * 50), "completed": True},
            "exercise_minutes": {"value": 30 if i > 1 else 45, "completed": True}
        }
        
        measurement_data = {
            "weight_kg": {"value": 72.5 - (i * 0.1)},
            "bpm_resting": {"value": 68 + (i % 3)}
        }
        
        symptom_entry = None
        if i == 3:
            symptom_entry = {"date": entry_date, "type": "головная_боль", "severity": 2}

        entries.append({
            "date": entry_date,
            "habits": habit_data,
            "measurements": measurement_data,
            "symptoms": [symptom_entry] if symptom_entry else []
        })

    with open("data.json", "w") as f:
        json.dump({"entries": entries}, f)
