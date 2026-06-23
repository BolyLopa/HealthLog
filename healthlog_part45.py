# === Stage 45: Add restore from backup with validation ===
# Project: HealthLog
import json, os, hashlib
from datetime import datetime

BACKUP_FILE = "healthlog_backup.json"
CURRENT_DATA_FILE = "data.json"

def validate_data_integrity(data):
    if not isinstance(data, dict) or 'entries' not in data:
        return False, "Invalid structure"
    for entry in data.get('entries', []):
        if not all(k in entry for k in ['date', 'type']):
            return False, f"Missing keys in entry {entry}"
    return True, None

def restore_from_backup():
    if os.path.exists(BACKUP_FILE) and os.path.exists(CURRENT_DATA_FILE):
        try:
            with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
                backup_data = json.load(f)
            
            valid, error_msg = validate_data_integrity(backup_data)
            if not valid:
                print(f"Backup validation failed: {error_msg}")
                return False
            
            with open(CURRENT_DATA_FILE, 'r', encoding='utf-8') as f:
                current_hash = hashlib.sha256(f.read()).hexdigest()
            
            backup_hash = hashlib.sha256(json.dumps(backup_data, sort_keys=True).encode()).hexdigest()
            
            if current_hash == backup_hash:
                print("Backup data is identical to current; no restore needed.")
                return False
            
            confirm = input("Restore from backup? (y/n): ").strip().lower()
            if confirm != 'y':
                print("Restore cancelled.")
                return False
                
            with open(CURRENT_DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(backup_data, f, indent=2)
            
            print("Data restored successfully from backup.")
            return True
            
        except Exception as e:
            print(f"Restore failed: {e}")
            return False
    else:
        if not os.path.exists(BACKUP_FILE):
            print("No backup file found.")
        elif not os.path.exists(CURRENT_DATA_FILE):
            print("Current data file missing; cannot compare hashes.")
        return False
