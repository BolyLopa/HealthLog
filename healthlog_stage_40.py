# === Stage 40: Add plain text report export ===
# Project: HealthLog
def export_weekly_report(logs, week_start):
    from datetime import timedelta, date
    end_date = week_start + timedelta(days=7)
    lines = ["HealthLog Weekly Report", "=" * 40]
    for d in range(7):
        curr = week_start + timedelta(days=d)
        day_logs = [l for l in logs if curr <= l['date'] < curr + timedelta(days=1)]
        if not day_logs: continue
        lines.append(f"\n{curr.strftime('%Y-%m-%d')}:")
        for log in sorted(day_logs, key=lambda x: x.get('type', '')):
            t = log.get('type', 'misc').upper()
            v = str(log.get('value', '')).strip() or '?'
            lines.append(f"  [{t}] {v}")
    if not any(d in logs for d in range(7) if week_start + timedelta(days=d)):
        lines.append("\nNo entries this week.")
    return "\n".join(lines)
