# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: HealthLog
def _format_date(date_str: str) -> str:
    """Convert ISO date string to YYYY-MM-DD format."""
    if isinstance(date_str, datetime):
        return date_str.strftime("%Y-%m-%d")
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Invalid ISO date format: {date_str}")


def _calculate_week_number(date_str: str) -> int:
    """Calculate the ISO week number for a given date string."""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.isocalendar()[1]
    except ValueError:
        raise ValueError(f"Invalid date format for week calculation: {date_str}")


def _group_entries_by_week(entries: List[Dict], date_field: str = "timestamp") -> Dict[int, List[Dict]]:
    """Group log entries by their ISO week number."""
    grouped = {}
    for entry in entries:
        try:
            week_num = _calculate_week_number(entry[date_field])
            if week_num not in grouped:
                grouped[week_num] = []
            grouped[week_num].append(entry)
        except (ValueError, KeyError):
            continue  # Skip invalid entries silently
    return grouped


def generate_weekly_summary(entries: List[Dict], date_field: str = "timestamp") -> Dict[int, Dict]:
    """Generate a summary report for each week containing entry counts and averages."""
    grouped = _group_entries_by_week(entries, date_field)
    summaries = {}
    for week_num, week_entries in sorted(grouped.items()):
        if not week_entries:
            continue
        
        # Calculate average heart rate from 'heart_rate' field if present
        hr_values = [e.get("heart_rate") for e in week_entries if "heart_rate" in e and e["heart_rate"] is not None]
        avg_hr = sum(hr_values) / len(hr_values) if hr_values else 0
        
        # Calculate average steps from 'steps' field if present
        step_values = [e.get("steps") for e in week_entries if "steps" in e and e["steps"] is not None]
        avg_steps = sum(step_values) / len(step_values) if step_values else 0
        
        summaries[week_num] = {
            "start_date": _format_date(week_entries[0][date_field]),
            "end_date": _format_date(week_entries[-1][date_field]),
            "entry_count": len(week_entries),
            "avg_heart_rate": round(avg_hr, 2) if avg_hr else None,
            "total_steps": sum(step_values) if step_values else None,
        }
    return summaries
