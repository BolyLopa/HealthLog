# === Stage 42: Add CSV export without external dependencies ===
# Project: HealthLog
def export_to_csv(records, filename="health_log.csv"):
    import csv
    if not records: return False
    headers = list(records[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for record in records:
            clean_record = {k: str(v) if v is not None else "" for k, v in record.items()}
            writer.writerow(clean_record)
    return True
