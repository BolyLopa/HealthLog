# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: HealthLog
def generate_changelog(log_entries):
    """Generate a compact changelog from activity log entries."""
    if not log_entries:
        return "No recent changes."
    
    lines = ["### Changelog"]
    seen_dates = set()
    current_date = None
    
    for entry in sorted(log_entries, key=lambda x: x.get('timestamp', ''), reverse=True):
        date_str = entry.get('date') or entry.get('timestamp', '').split('T')[0] if isinstance(entry.get('timestamp'), str) else ''
        
        if not date_str:
            continue
            
        if date_str in seen_dates:
            lines.append(f"- {entry.get('action')}")
        else:
            seen_dates.add(date_str)
            lines.append(f"#### {date_str}")
            lines.append(f"- {entry.get('action')}")
            
    return "\n".join(lines)
