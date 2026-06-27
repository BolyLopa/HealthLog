# === Stage 58: Add bulk update behavior for selected records ===
# Project: HealthLog
from typing import List, Optional
def bulk_update_records(records: List[dict], updates: dict) -> List[dict]:
    """Apply common fields to a list of records and return the updated list."""
    if not records or not updates:
        return records.copy()
    result = []
    for r in records:
        new_r = {**r, **updates}
        # Ensure specific keys like 'id' are preserved from original record
        if 'id' in r and 'id' not in updates:
            new_r['id'] = r['id']
        result.append(new_r)
    return result

def bulk_set_status(records: List[dict], status: str, field_name: Optional[str] = None) -> List[dict]:
    """Set a specific status on all records or use the first available status field if not specified."""
    updates = {'status': status}
    if field_name and 'status' in updates:
        updates[field_name] = status
    return bulk_update_records(records, updates)

def bulk_add_tags(records: List[dict], tags: List[str]) -> List[dict]:
    """Append provided tags to the existing tag list of each record."""
    if not records or not tags:
        return records.copy()
    result = []
    for r in records:
        current_tags = r.get('tags', [])
        # Avoid duplicates while preserving order
        combined = current_tags + [t for t in tags if t not in current_tags]
        new_r = {**r, 'tags': combined}
        result.append(new_r)
    return result

def bulk_filter_by_date(records: List[dict], start_date: str, end_date: str) -> List[dict]:
    """Filter records by date range assuming a 'date' field exists in each record."""
    if not records or 'date' not in records[0]:
        return []
    filtered = [r for r in records if start_date <= r['date'] <= end_date]
    return bulk_update_records(filtered, {'filtered': True})

def bulk_apply_formula(records: List[dict], field_name: str, formula_func) -> List[dict]:
    """Apply a function to calculate new values for a specific field in all records."""
    if not records or 'date' not in records[0]:
        return records.copy()
    result = []
    for r in records:
        try:
            val = formula_func(r.get('value', 0), r['date'])
            new_r = {**r, field_name: val}
            result.append(new_r)
        except Exception:
            # Keep original if calculation fails
            result.append(r.copy())
    return result
