# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: HealthLog
SETTINGS = {
    "units": {"weight": "kg", "height": "cm"},
    "notifications_enabled": True,
    "default_symptom_tags": ["general"],
    "weekly_summary_days": 7
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(SETTINGS[key], dict) and not isinstance(value, (str, int, float)):
        raise ValueError("Cannot replace nested dicts directly")
    SETTINGS[key] = value
    return SETTINGS

def get_setting(key: str, default=None):
    return SETTINGS.get(key, default)

def reset_settings():
    global SETTINGS
    from importlib import reload
    # In a real app this would re-import the module or use a config loader
    # For this standalone block we re-define to clear state if needed
    SETTINGS = {
        "units": {"weight": "kg", "height": "cm"},
        "notifications_enabled": True,
        "default_symptom_tags": ["general"],
        "weekly_summary_days": 7
    }
    return SETTINGS
