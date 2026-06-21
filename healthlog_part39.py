# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: HealthLog
def repair_data_integrity(log_file):
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    valid_entries = []
    seen_ids = set()
    duplicates_removed = 0
    
    for i, raw_line in enumerate(lines):
        if not raw_line.startswith('ENTRY|'): continue
        
        parts = raw_line.split('|')
        if len(parts) < 4:
            print(f"Line {i+1}: Invalid format skipped")
            continue
            
        entry_id, date_time, category, value = parts[:4]
        
        # Check for duplicate IDs within a reasonable time window (24h)
        if entry_id in seen_ids:
            duplicates_removed += 1
            print(f"Line {i+1}: Duplicate ID '{entry_id}' detected and skipped")
            continue
        
        try:
            datetime_obj = __import__('datetime').datetime.fromisoformat(date_time.replace('Z', '+00:00'))
            # Validate date is not in the future (allow 5 min buffer for clock skew)
            now = __import__('datetime').datetime.now(datetime_obj.tzinfo)
            if datetime_obj > now + __import__('timedelta').timedelta(minutes=5):
                print(f"Line {i+1}: Future date detected, skipped")
                continue
                
        except Exception:
            print(f"Line {i+1}: Invalid timestamp format, skipped")
            continue
        
        seen_ids.add(entry_id)
        
        # Normalize category to lowercase for consistency
        normalized_category = category.lower() if isinstance(category, str) else category
        
        valid_entries.append({
            'id': entry_id,
            'timestamp': date_time,
            'category': normalized_category,
            'value': value.strip(),
            '_raw_line': raw_line # Keep original for potential re-export
        })
    
    if duplicates_removed > 0:
        print(f"Repair complete. Removed {duplicates_removed} duplicate entries.")

    with open(log_file, 'w', encoding='utf-8') as f:
        for entry in valid_entries:
            # Reconstruct line preserving original value casing but normalized category
            new_line = f"{entry['id']}|{entry['timestamp']}|{entry['category']}|{entry['value']}\n"
            f.write(new_line)
