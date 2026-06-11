# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: HealthLog
def format_entry(entry):
    if entry.get('type') == 'habit':
        status = "✓" if entry.get('completed') else "✗"
        return f"[{status}] {entry['name']}"
    elif entry.get('type') == 'measurement':
        unit = entry.get('unit', '')
        return f"{entry['value']} {unit}"
    elif entry.get('type') == 'symptom':
        severity = entry.get('severity', 'mild')
        return f"⚠ {entry['description']} ({severity})"
    return str(entry)

def format_week_summary(week_data):
    lines = ["=== Weekly Summary ==="]
    if week_data.get('habits'):
        completed = sum(1 for h in week_data['habits'] if h.get('completed'))
        total = len(week_data['habits'])
        lines.append(f"Habits: {completed}/{total} completed")
    if week_data.get('measurements'):
        lines.append("Measurements:")
        for m in week_data['measurements']:
            lines.append(format_entry(m))
    if week_data.get('symptoms'):
        lines.append("Symptoms:")
        for s in week_data['symptoms']:
            lines.append(format_entry(s))
    return "\n".join(lines)
