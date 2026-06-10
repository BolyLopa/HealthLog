# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: HealthLog
def update_record(db, record_id, updates):
    """
    Update an existing record (habit, measurement, symptom) by ID.
    Handles missing records gracefully by returning a status message.
    Only provided fields are updated; others remain unchanged.
    Expects 'db' to be a dict or simple object with 'get' and 'set' methods.
    """
    if not db:
        return {"status": "error", "message": "Database is empty or invalid."}

    record = db.get(record_id)
    if not record:
        return {"status": "not_found", "message": f"Record with ID {record_id} does not exist."}

    # Merge updates into existing record without overwriting unknown keys
    for key, value in updates.items():
        if key in record:
            record[key] = value
        else:
            return {"status": "error", "message": f"Unknown field '{key}' for record type {record.get('type', 'unknown')}."}

    # Optional: Update timestamp if provided
    if "timestamp" in updates:
        record["timestamp"] = updates["timestamp"]

    return {"status": "success", "message": f"Record {record_id} updated.", "data": record}
