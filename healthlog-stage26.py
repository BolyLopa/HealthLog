# === Stage 26: Add weekly summary calculations ===
# Project: HealthLog
def calculate_weekly_summary(records, week_start):
    from datetime import timedelta, date
    week_end = week_start + timedelta(days=7)
    weekly_data = {d: [] for d in range(week_start.weekday(), (week_end - timedelta(days=1)).weekday() + 1)}
    
    def to_date_key(dt):
        return dt.date().isocalendar()[0], dt.date().isocalendar()[1]

    filtered = [r for r in records if week_start <= r['timestamp'] < week_end]
    
    if not filtered:
        return {"status": "no_data", "message": f"No data found for week {week_start.isoformat()}", "metrics": []}
    
    metrics = {}
    for entry in filtered:
        key = to_date_key(entry['timestamp'])
        daily_metrics = weekly_data[key]
        
        if 'weight' in entry and entry.get('value') is not None:
            d = {**daily_metrics, "weight": entry["value"]}
            metrics.setdefault("weight", []).append(d)
        elif 'steps' in entry and entry.get('value') is not None:
            d = {**daily_metrics, "steps": entry["value"]}
            metrics.setdefault("steps", []).append(d)
        elif 'sleep_hours' in entry and entry.get('value') is not None:
            d = {**daily_metrics, "sleep": entry["value"]}
            metrics.setdefault("sleep", []).append(d)
    
    summary = {"week_start": week_start.isoformat(), "metrics_summary": []}
    for metric_name, daily_list in sorted(metrics.items()):
        if not daily_list:
            continue
        
        total = sum(item.get(metric_name.replace("_hours", "").replace("sleep", ""), 0) for item in daily_list)
        avg = round(total / len(daily_list), 2) if daily_list else 0
        max_val = max((item.get(metric_name.replace("_hours", "").replace("sleep", ""), 0) for item in daily_list), default=0)
        
        summary["metrics_summary"].append({
            "metric": metric_name,
            "total": total,
            "average": avg,
            "max": max_val,
            "days_recorded": len(daily_list)
        })
    
    return summary
