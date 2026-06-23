# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: HealthLog
import datetime, random

def run_demo():
    user = {"name": "Demo User", "habits": ["Drink Water"], "measurements": [], "symptoms": []}
    today = datetime.date.today()
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        habit_check = random.choice([True, False])
        if user["habits"][0] == "Drink Water" and habit_check:
            user["measurements"].append({"date": date.isoformat(), "value": f"{random.randint(1500, 3000)} ml"})
        else:
            user["measurements"].append({"date": date.isoformat(), "value": None})
        symptom = random.choice(["None", "Headache", "Fatigue"])
        if symptom != "None":
            user["symptoms"].append({"date": date.isoformat(), "description": symptom})
    print(f"Welcome, {user['name']}! Here is your weekly summary:")
    for m in sorted(user["measurements"], key=lambda x: x["date"]):
        status = f"{m['value']}" if m["value"] else "Skipped"
        print(f"  {m['date']}: Habit {'✓' if m['value'] else '✗'}, Measurement: {status}")
    for s in sorted(user["symptoms"], key=lambda x: x["date"]):
        print(f"  {s['date']}: Symptom reported - {s['description']}")
