# === Stage 41: Add plain text import for a simple line-based format ===
# Project: HealthLog
def parse_simple_log(filename):
    records = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) != 4:
                continue
            date_str, habit_type, value, notes = parts
            try:
                records.append({
                    'date': datetime.strptime(date_str, '%Y-%m-%d'),
                    'type': habit_type,
                    'value': float(value),
                    'notes': notes if notes else ''
                })
            except ValueError:
                continue
    return sorted(records, key=lambda x: x['date'])
