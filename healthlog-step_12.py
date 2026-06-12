# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: HealthLog
import json, os, sys

def load_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        error_msg = str(e).split("'")[1].replace('"', '') if "'" in str(e) else str(e)
        print(f"[ERROR] Malformed JSON at '{path}': {error_msg[:50]}...")
        return {}

def save_json_safe(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save '{path}': {e}")
        return False

if __name__ == "__main__":
    config_path = "config.json"
    data = load_json_safe(config_path)
    if not data:
        sys.exit(1)
