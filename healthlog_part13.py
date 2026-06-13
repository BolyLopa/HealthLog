# === Stage 13: Add file save support using a configurable path ===
# Project: HealthLog
import os, json, sys
from pathlib import Path
try:
    from health_log_core import HealthLog
except ImportError: pass

def get_config_path():
    cfg = Path.home() / ".healthlog" / "config.json"
    if not cfg.exists():
        cfg.parent.mkdir(parents=True, exist_ok=True)
        return str(cfg)
    return cfg

def save_log(log_obj):
    path = get_config_path()
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump({
                "user": log_obj.user,
                "habits": log_obj.habits,
                "measurements": log_obj.measurements,
                "symptoms": log_obj.symptoms,
                "weekly_summaries": log_obj.weekly_summaries
            }, f, indent=2)
        print(f"Saved to {path}")
    except Exception as e:
        sys.stderr.write(f"Save error: {e}\n")

if __name__ == "__main__":
    save_log(HealthLog("Alice", {"water": 1500}, [{"temp": 36.6}], []))
