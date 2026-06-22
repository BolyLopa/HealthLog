# === Stage 44: Add backup creation for the data file ===
# Project: HealthLog
import os, json, datetime, shutil
from pathlib import Path

def backup_data(data_file: str) -> None:
    """Create a timestamped backup of the current data file."""
    if not os.path.exists(data_file):
        return
    
    path = Path(data_file)
    parent_dir = path.parent
    backups_dir = parent_dir / "backups"
    
    try:
        shutil.copy2(path, backups_dir / f"{path.name}.{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_data("health_log.json")
