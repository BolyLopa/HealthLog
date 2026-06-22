# === Stage 43: Add CSV import for the primary record type ===
# Project: HealthLog
import csv
from pathlib import Path

def load_records_from_csv(file_path: str, record_type: str) -> list[dict]:
    records = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('type', '').strip().lower() == record_type.lower():
                records.append({k.strip(): v.strip() for k, v in row.items()})
    return records

def merge_csv_records(existing_data: list[dict], csv_file_path: str) -> None:
    new_records = load_records_from_csv(csv_file_path, 'habit')
    existing_data.extend(new_records)
