# === Stage 20: Add duplicate detection for newly created records ===
# Project: HealthLog
from datetime import date, timedelta

def get_week_key(record_date: date) -> str:
    return record_date.strftime("%Y-W%W")

class DuplicateDetector:
    def __init__(self, existing_records):
        self.weekly_summaries = {}
        for rec in existing_records:
            week = get_week_key(rec['date'])
            if week not in self.weekly_summaries:
                self.weekly_summaries[week] = []
            self.weekly_summaries[week].append(rec)

    def is_duplicate(self, new_record: dict) -> bool:
        current_date = date.fromisoformat(new_record['date'])
        week_key = get_week_key(current_date)
        if week_key not in self.weekly_summaries:
            return False
        
        existing_in_week = self.weekly_summaries[week_key]
        
        for existing_rec in existing_in_week:
            if (existing_rec.get('type') == new_record['type'] and 
                abs(existing_rec['value'] - float(new_record['value'])) < 0.1):
                return True
                
        return False

    def get_similar_records(self, new_record: dict) -> list:
        current_date = date.fromisoformat(new_record['date'])
        week_key = get_week_key(current_date)
        
        if week_key not in self.weekly_summaries:
            return []
            
        existing_in_week = self.weekly_summaries[week_key]
        similar = []
        
        for existing_rec in existing_in_week:
            if (existing_rec.get('type') == new_record['type'] and 
                abs(existing_rec['value'] - float(new_record['value'])) < 0.1):
                similar.append(existing_rec)
                
        return similar
