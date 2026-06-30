# === Stage 67: Add a function that returns key project metrics ===
# Project: HealthLog
def get_project_metrics(db):
    """Return key project metrics from the database."""
    import sqlite3
    
    conn = db.connect()
    
    # Total number of entries (habits, measurements, symptoms)
    total_entries = sum(conn.execute("SELECT COUNT(*) FROM habits").fetchone()[0],
                        conn.execute("SELECT COUNT(*) FROM measurements").fetchone()[0],
                        conn.execute("SELECT COUNT(*) FROM symptoms").fetchone()[0])
    
    # Total number of users (if a users table exists)
    try:
        total_users = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    except sqlite3.OperationalError:
        total_users = 1
    
    # Average daily habits completed in the last 7 days
    avg_habits_last_week = conn.execute("""
        SELECT AVG(habit_count) 
        FROM (
            SELECT COUNT(*) AS habit_count, DATE(date) as day
            FROM habits
            WHERE date >= datetime('now', '-7 days')
            GROUP BY day
        )
    """).fetchone()[0] or 0.0
    
    # Most frequent symptom category (if symptoms have a category column)
    try:
        most_frequent_symptom = conn.execute("""
            SELECT symptom, COUNT(*) as count 
            FROM symptoms 
            GROUP BY symptom 
            ORDER BY count DESC 
            LIMIT 1
        """).fetchone()
        top_symptom = most_frequent_symptom[0] if most_frequent_symptom else None
    except sqlite3.OperationalError:
        top_symptom = None
    
    conn.close()
    
    return {
        "total_entries": total_entries,
        "total_users": total_users,
        "avg_habits_last_week": avg_habits_last_week,
        "top_symptom": top_symptom
    }
