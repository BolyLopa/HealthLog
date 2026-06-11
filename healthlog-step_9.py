# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: HealthLog
def sort_entries(entries, key='date', reverse=False):
    if key == 'title': return sorted(entries, key=lambda e: (e.get('priority') or 0, e['title']), reverse=reverse)
    if key == 'priority': return sorted(entries, key=lambda e: (e.get('priority') or 0, -int(e.get('date', ''))), reverse=True)
    if key == 'last_update': return sorted(entries, key=lambda e: e.get('updated_at', ''), reverse=reverse)
    if key == 'date': return sorted(entries, key=lambda e: e['date'], reverse=reverse)
    return entries

def get_weekly_summary(data):
    from datetime import datetime, timedelta
    today = datetime.now()
    week_start = (today - timedelta(days=today.weekday())).strftime('%Y-%m-%d')
    weekly_data = {k: [] for k in ['habits', 'measurements', 'symptoms']}
    for entry in data:
        if entry['date'] >= week_start:
            category = list(weekly_data.keys())[list(map(lambda x: x == entry.get('category'), ['habits', 'measurements', 'symptoms']))]
            weekly_data[category].append(entry)
    return {k: sorted(v, key=lambda e: e['date'], reverse=True) for k, v in weekly_data.items()}
