# === Stage 73: Add a lightweight HTML report export ===
# Project: HealthLog
import json, datetime, os

def export_report(logs_file="health_log.json", output_html="report.html"):
    if not os.path.exists(logs_file): return
    with open(logs_file) as f: data = json.load(f)
    logs = data.get("entries", [])
    today = datetime.date.today().isoformat()
    week_start = (datetime.datetime.now() - datetime.timedelta(days=datetime.datetime.now().weekday())).date().isoformat()
    weekly_logs = [e for e in logs if e["date"] >= week_start]
    html_parts = ["<!DOCTYPE html><html><head><style>body{font-family:sans-serif;padding:20px;}.entry{border-bottom:1px solid #ccc;margin-bottom:15px;}table{width:100%;margin-top:5px;border-collapse:collapse;}</style></head><body>", "<h1>HealthLog Report</h1>", f"<p>Last updated: {today}</p>"]
    if weekly_logs: html_parts.append("<h2>This Week's Activity</h2>")
    for e in weekly_logs: html_parts.append(f'<div class="entry"><strong>{e["date"]}:</strong><br>Habit: {e.get("habit", "N/A")}<br>Measurement: {e.get("measurement", "N/A")} mmHg<br>Symptom: {e.get("symptom", "None")}</div>')
    html_parts.append("</body></html>")
    with open(output_html, "w") as f: f.write("\n".join(html_parts))
