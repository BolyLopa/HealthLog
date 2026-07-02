# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: HealthLog
def seed_demo_data(db):
    from datetime import date, timedelta
    user = db["users"].find_one({"username": "demo"})
    if not user:
        db["users"].insert_one({"username": "demo", "name": "Demo User", "email": "demo@example.com"})
    user_id = db.get_collection("users").insert_one({"username": "demo"}).inserted_id
    habits = [
        {"id": 1, "title": "Drink Water", "target": 2000},
        {"id": 2, "title": "Read Book", "target": 30}
    ]
    for h in habits:
        db["habits"].insert_one({"user_id": user_id, **h})
    measurements = [
        {"date": date.today() - timedelta(days=1), "type": "weight", "value": 72.5},
        {"date": date.today(), "type": "steps", "value": 8400}
    ]
    for m in measurements:
        db["measurements"].insert_one({"user_id": user_id, **m})
    symptoms = [
        {"date": date.today() - timedelta(days=2), "severity": 1, "notes": "Slight headache"},
        {"date": date.today(), "severity": 0, "notes": ""}
    ]
    for s in symptoms:
        db["symptoms"].insert_one({"user_id": user_id, **s})
