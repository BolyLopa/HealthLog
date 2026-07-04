# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: HealthLog
import sys, json, datetime as dt
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from health_log import HealthLog  # Adjust import path to match your project structure

def run_self_check():
    log = HealthLog()
    
    print("=== HealthLog Self-Check & Demo ===")
    try:
        # 1. Create sample data for demo
        today = dt.date.today().isoformat()
        log.add_habit(name="Drink Water", date=today, value=2500)
        log.add_measurement(type="Weight", date=today, value=74.5, unit="kg")
        log.add_symptom(description="Headache", severity=3, date=today)
        
        # 2. Validate data integrity (basic checks)
        assert len(log.habits) > 0, "Habits list is empty"
        assert len(log.measurements) > 0, "Measurements list is empty"
        print("✓ Data validation passed.")
        
        # 3. Generate weekly summary for current week
        start_of_week = (today - dt.timedelta(days=today.weekday())).isoformat()
        end_of_week = today.isoformat()
        summary = log.generate_summary(start=start_of_week, end=end_of_week)
        
        print(f"\n--- Weekly Summary ({start_of_week} to {end_of_week}) ---")
        if summary:
            for key, val in summary.items():
                print(f"{key}: {val}")
        else:
            print("No data found for this week.")
            
        # 4. Export demo state to JSON (if writable)
        export_path = Path(__file__).parent / "demo_export.json"
        try:
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(log.to_dict(), f, indent=2, ensure_ascii=False)
            print(f"\n✓ Demo data exported to {export_path.name}")
        except PermissionError:
            print("\n⚠ Cannot write export file (permission denied).")
            
    except Exception as e:
        print(f"✗ Error during self-check: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_self_check()
