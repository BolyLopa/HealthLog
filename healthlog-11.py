# === Stage 11: Add JSON export for the current application state ===
# Project: HealthLog
def export_state_json():
    import json, os
    data = {
        "habits": habits,
        "measurements": measurements,
        "symptoms": symptoms,
        "last_updated": datetime.now().isoformat()
    }
    filename = "healthlog_export.json"
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] State exported to {filename}")
    except Exception as e:
        print(f"[ERROR] Export failed: {e}")
