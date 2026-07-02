# === Stage 72: Add Markdown report export ===
# Project: HealthLog
def export_weekly_report(data, start_date):
    from datetime import timedelta, date
    end_date = start_date + timedelta(days=7)
    lines = ["# Weekly Wellness Report", f"Period: {start_date} to {end_date}", ""]
    for habit in data.get("habits", []):
        if habit["name"]:
            count = sum(1 for d, v in data.get("measurements", {}).items() if d >= start_date and d < end_date and v.get(habit["name"], 0) > 0)
            lines.append(f"- {habit['name']}: completed {count} times")
    symptoms = [s for s in data.get("symptoms", []) if s.get("date", date.today()) >= start_date]
    if symptoms:
        lines.append("")
        lines.append("## Symptoms Log")
        for sym in sorted(symptoms, key=lambda x: x["date"]):
            lines.append(f"- {sym['description']} on {sym['date'].strftime('%Y-%m-%d')}")
    return "\n".join(lines)
