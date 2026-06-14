# === Stage 18: Add an activity log with timestamps and action names ===
# Project: HealthLog
from datetime import datetime, timedelta
import random

class ActivityLog:
    def __init__(self):
        self.entries = []

    def log_activity(self, action_name, duration_minutes=None):
        entry = {
            "timestamp": datetime.now(),
            "action": action_name,
            "duration": duration_minutes
        }
        self.entries.append(entry)
        return entry

    def get_recent_activities(self, days=7):
        cutoff = datetime.now() - timedelta(days=days)
        recent = [e for e in self.entries if e["timestamp"] > cutoff]
        return sorted(recent, key=lambda x: x["timestamp"], reverse=True)[:10]

    def generate_weekly_summary(self):
        week_start = (datetime.now().date() - timedelta(days=datetime.now().weekday())).replace(hour=0, minute=0, second=0)
        weekly_activities = [e for e in self.entries if e["timestamp"] >= week_start]
        
        total_actions = len(weekly_activities)
        total_duration = sum(e.get("duration", 0) for e in weekly_activities)
        
        action_counts = {}
        for act in weekly_activities:
            name = act["action"]
            action_counts[name] = action_counts.get(name, 0) + 1
            
        summary_text = f"Weekly Activity Summary (Last 7 days):\nTotal Actions: {total_actions}\nTotal Duration: {total_duration} minutes\n"
        if action_counts:
            sorted_actions = sorted(action_counts.items(), key=lambda x: x[1], reverse=True)
            for name, count in sorted_actions[:5]:
                summary_text += f"- {name}: {count} times\n"
        else:
            summary_text += "No activities recorded this week.\n"
            
        return summary_text

# Example usage within the main script context
if __name__ == "__main__":
    log = ActivityLog()
    
    # Simulate some random activities for demonstration
    sample_actions = ["Walk", "Read", "Meditate", "Exercise", "Drink Water"]
    for _ in range(random.randint(5, 15)):
        action = random.choice(sample_actions)
        duration = random.choice([None] + [random.randint(5, 60)] * (3 if action == "Walk" else []))
        log.log_activity(action, duration=duration)

    print(log.generate_weekly_summary())
