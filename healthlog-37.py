# === Stage 37: Add recommendations for the next useful action ===
# Project: HealthLog
from datetime import date, timedelta
import random
from typing import Optional, Dict, Any

def generate_weekly_recommendation(log_data: Dict[str, Any]) -> str:
    """Generates a concise recommendation based on weekly trends."""
    if not log_data.get("measurements"):
        return "Start tracking your daily measurements to identify patterns."
    
    avg_sleep = sum(m.get("sleep_hours", 0) for m in log_data["measurements"]) / max(len(log_data["measurements"]), 1)
    avg_steps = sum(m.get("steps", 0) for m in log_data["measurements"]) / max(len(log_data["measurements"]), 1)
    
    if avg_sleep < 7:
        return f"Your average sleep is {avg_sleep:.1f}h. Aim for at least 7 hours tonight."
    elif avg_steps < 5000:
        return "You walked less than 5k steps this week. Try a 20-minute walk today."
    else:
        symptoms = log_data.get("symptoms", [])
        if any(s in ["headache", "fatigue"] for s in symptoms):
            return "Rest and hydrate; your recent symptoms suggest you need recovery time."
        return f"Great job! Keep up the momentum. Next step: review next week's goals."

def log_recommendation(user_id: str, recommendation: str) -> None:
    """Appends a new record to the user's recommendations list."""
    today = date.today()
    entry = {
        "date": today.isoformat(),
        "user_id": user_id,
        "recommendation": recommendation,
        "timestamp": random.randint(1000, 9999) # Simulating a unique ID for sorting if needed later
    }
    
    with open(f"logs/{user_id}_recs.json", "a") as f:
        f.write("\n" + str(entry))
