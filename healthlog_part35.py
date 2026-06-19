# === Stage 35: Add active user switching and user-specific records ===
# Project: HealthLog
class UserSwitcher:
    def __init__(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()
        self._create_users_table()
    
    def _create_users_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.db.commit()
    
    def add_user(self, name):
        try:
            self.cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            self.db.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def switch_to(self, user_name):
        self.cursor.execute("SELECT id FROM users WHERE name = ?", (user_name,))
        row = self.cursor.fetchone()
        if row:
            self.current_user_id = row[0]
            return True
        return False
