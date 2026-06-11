# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: HealthLog
def filter_logs(logs, filters=None):
    if filters is None:
        filters = {}
    
    filtered = []
    for log in logs:
        match = True
        
        if 'status' in filters and log.get('status') != filters['status']:
            match = False
        elif 'category' in filters and log.get('category') != filters['category']:
            match = False
        elif 'owner' in filters and log.get('owner') != filters['owner']:
            match = False
        elif 'tag' in filters and filters['tag'] not in log.get('tags', []):
            match = False
            
        if match:
            filtered.append(log)
    
    return filtered
