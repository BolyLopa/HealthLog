# === Stage 28: Add overdue item detection based on due dates ===
# Project: HealthLog
from datetime import date, timedelta
def check_overdue_items(log_entries):
    today = date.today()
    overdue_list = []
    for entry in log_entries:
        if 'due_date' in entry and isinstance(entry['due_date'], str):
            due = date.fromisoformat(entry['due_date'])
            days_diff = (today - due).days
            if days_diff > 0:
                overdue_list.append({
                    "id": entry["id"],
                    "name": entry.get("name", "Unknown"),
                    "due_date": entry["due_date"],
                    "overdue_days": days_diff,
                    "status": entry.get("status", "pending")
                })
    return overdue_list

def generate_overdue_summary(overdue_items):
    if not overdue_items:
        return "No overdue items found."
    total_overdue = len(overdue_items)
    critical_count = sum(1 for item in overdue_items if item["overdue_days"] > 7)
    summary = f"Found {total_overdue} overdue habit(s).\nCritical (>7 days): {critical_count}\nDetails:\n"
    for item in overdue_items:
        summary += f"- [{item['name']}] Due: {item['due_date']} (Overdue by {item['overdue_days']} days)\n"
    return summary

if __name__ == "__main__":
    sample_data = [
        {"id": 1, "name": "Morning Jog", "status": "pending", "due_date": "2023-10-01"},
        {"id": 2, "name": "Water Intake", "status": "completed", "due_date": "2024-05-20"},
        {"id": 3, "name": "Meditation", "status": "pending", "due_date": date.today().isoformat()}
    ]
    overdue = check_overdue_items(sample_data)
    if overdue:
        print(generate_overdue_summary(overdue))
