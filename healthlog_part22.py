# === Stage 22: Add favorite records and quick favorite listing ===
# Project: HealthLog
class FavoriteManager:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, record_id TEXT UNIQUE)")
    
    def add_favorite(self, record_id):
        try:
            self.cursor.execute("INSERT INTO favorites (record_id) VALUES (?)", (record_id,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def remove_favorite(self, record_id):
        self.cursor.execute("DELETE FROM favorites WHERE record_id = ?", (record_id,))
        self.db.commit()
    
    def get_favorites(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT record_id FROM favorites ORDER BY id")
        return [row[0] for row in cursor.fetchall()]

def load_favorite_records(fav_manager, data_loader):
    fav_ids = fav_manager.get_favorites()
    if not fav_ids:
        print("No favorite records found.")
        return []
    
    favorites = []
    for record_id in fav_ids:
        try:
            rec = data_loader.load_record(record_id)
            if rec:
                favorites.append(rec)
        except Exception as e:
            print(f"Error loading record {record_id}: {e}")
    return favorites
