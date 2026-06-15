# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: HealthLog
from datetime import datetime, timedelta
import json
import os

def archive_records(records_path, archive_dir='archive', days_threshold=30):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archived_count = 0
    
    with open(records_path, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        new_lines = []
        for line in lines:
            try:
                record = json.loads(line.strip())
                if record.get('completed', False) or datetime.fromisoformat(record['timestamp'][:19]) < cutoff_date:
                    archive_name = f"{record['id']}_{'completed' if record.get('completed') else 'old'}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    with open(os.path.join(archive_dir, archive_name), 'w', encoding='utf-8') as af:
                        af.write(line)
                    archived_count += 1
                else:
                    new_lines.append(line)
            except json.JSONDecodeError:
                new_lines.append(line)
        
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)
    
    return archived_count

def restore_records(records_path, archive_dir='archive', target_id=None):
    if not os.path.exists(archive_dir):
        return 0
    
    restored = False
    with open(records_path, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        
        for filename in sorted(os.listdir(archive_dir)):
            if target_id and not str(target_id) in filename:
                continue
            
            archive_path = os.path.join(archive_dir, filename)
            with open(archive_path, 'r', encoding='utf-8') as af:
                content = af.read()
            
            lines.insert(lines.index(content), content + '\n' if lines else '')
            try:
                record = json.loads(content.strip())
                os.remove(archive_path)
                restored = True
                print(f"Restored {filename} to main log.")
            except json.JSONDecodeError:
                pass
    
    with open(records_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    return 1 if restored else 0
