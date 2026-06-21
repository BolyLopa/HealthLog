# === Stage 38: Add data integrity checks for broken references ===
# Project: HealthLog
class DataIntegrityChecker:
    def __init__(self, db):
        self.db = db
    
    def check_orphaned_measurements(self):
        user_ids = {row['user_id'] for row in self.db.execute("SELECT DISTINCT user_id FROM users")}
        orphaned = [m for m in self.db.execute("SELECT * FROM measurements WHERE user_id NOT IN ?", (tuple(user_ids),))]
        if orphaned:
            print(f"Found {len(orphaned)} orphaned measurements. Consider deleting or assigning them.")
    
    def check_invalid_symptom_references(self):
        symptom_names = {row['name'] for row in self.db.execute("SELECT name FROM symptoms")}
        invalid_refs = [s for s in self.db.execute("SELECT * FROM logs WHERE symptom_name NOT IN ?", (tuple(symptom_names),))]
        if invalid_refs:
            print(f"Found {len(invalid_refs)} logs referencing non-existent symptoms.")
    
    def check_broken_habit_links(self):
        habit_ids = {row['id'] for row in self.db.execute("SELECT id FROM habits")}
        broken = [h for h in self.db.execute("SELECT * FROM daily_logs WHERE habit_id NOT IN ?", (tuple(habit_ids),))]
        if broken:
            print(f"Found {len(broken)} daily logs referencing non-existent habits.")
    
    def run_all_checks(self):
        self.check_orphaned_measurements()
        self.check_invalid_symptom_references()
        self.check_broken_habit_links()
