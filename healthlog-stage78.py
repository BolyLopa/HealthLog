# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: HealthLog
def calculate_weekly_summary(records):
    if not records:
        return {"avg_habits": 0, "max_measurements": 0, "symptom_count": 0}
    
    habit_scores = [r.get("habit_score", 0) for r in records]
    measurements = [r.get("measurement_value") for r in records if r.get("measurement_type")]
    symptoms = [r for r in records if r.get("symptoms")]
    
    return {
        "avg_habits": sum(habit_scores) / len(records),
        "max_measurements": max(measurements, default=0),
        "symptom_count": len(symptoms)
    }

def format_weekly_report(summary):
    lines = [f"Week Summary:", f"Average Habits: {summary['avg_habits']:.1f}", 
             f"Max Measurement: {summary['max_measurements']}", 
             f"Symptom Occurrences: {summary['symptom_count']}"]
    return "\n".join(lines)
