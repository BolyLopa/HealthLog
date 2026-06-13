# === Stage 14: Add file load support with fallback demo data ===
# Project: HealthLog
def load_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "habits": [{"name": "Drink Water", "completed": True}],
            "measurements": [{"type": "Weight", "value": 70.5, "unit": "kg"}],
            "symptoms": [],
            "weekly_summary": "Start of new log."
        }
