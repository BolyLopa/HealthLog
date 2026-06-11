# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: HealthLog
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query.strip():
            return []
        
        q = query.lower()
        results = []
        
        for entry in self.data:
            text_fields = [
                str(entry.get('habit', '')),
                str(entry.get('measurement_value', '')),
                str(entry.get('symptom', '')),
                str(entry.get('notes', ''))
            ]
            
            if any(q in field for field in text_fields):
                results.append(entry)
        
        return results
