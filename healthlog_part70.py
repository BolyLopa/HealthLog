# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: HealthLog
import sys, os, json, hashlib
from datetime import datetime

def clear_state():
    if len(sys.argv) < 2:
        print("Usage: python healthlog.py clear-state")
        return False
    
    confirm_flag = "clear" in sys.argv[1].lower() or "-y" in sys.argv[1]
    
    if not confirm_flag:
        print("WARNING: Clearing all data requires explicit confirmation.")
        print("Run with 'clear-state -y' to proceed immediately,")
        print("or include 'clear' as the first argument after this command.")
        return False
    
    db_path = "healthlog_data.json"
    
    if not os.path.exists(db_path):
        print(f"No data file found at {db_path}. Nothing to clear.")
        return True
        
    try:
        with open(db_path, 'r') as f:
            data = json.load(f)
        
        # Clear all sections while preserving structure for future use
        if "habits" in data: data["habits"] = {}
        if "measurements" in data: data["measurements"] = []
        if "symptoms" in data: data["symptoms"] = []
        if "weekly_summaries" in data: data["weekly_summaries"] = []
        
        # Preserve user settings if they exist separately or reset timestamp
        if "settings" not in data:
            data["settings"] = {"version": 1, "last_reset": datetime.now().isoformat()}
            
        with open(db_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print("HealthLog state cleared successfully.")
        return True
        
    except Exception as e:
        print(f"Error clearing data: {e}")
        return False

if __name__ == "__main__":
    clear_state()
