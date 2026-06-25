# === Stage 53: Add command help text and usage examples ===
# Project: HealthLog
import argparse
from datetime import date, timedelta

def print_help():
    parser = argparse.ArgumentParser(prog='healthlog', description="Personal wellness log with habits and summaries.")
    parser.add_argument("--habit", "-h", help="Log a new habit (e.g., 'water:200ml')")
    parser.add_argument("--symptom", "-s", help="Record a symptom (e.g., 'headache:mild')")
    parser.add_argument("--measure", "-m", help="Add a measurement (e.g., 'weight:75.5kg')")
    parser.add_argument("--week", "-w", type=int, help="Generate weekly summary for week N (1-based)")
    parser.add_argument("--clear", "-c", action="store_true", help="Clear all local data")
    
    args = parser.parse_args()
    
    print("\n=== HealthLog Help ===")
    print("Usage: python healthlog.py [OPTIONS]")
    print("")
    if args.habit:
        print(f"Logged habit: {args.habit}")
    elif args.symptom:
        print(f"Logged symptom: {args.symptom}")
    elif args.measure:
        print(f"Logged measurement: {args.measure}")
    elif args.week is not None:
        week_start = date.today() - timedelta(weeks=args.week)
        week_end = week_start + timedelta(days=6)
        print(f"Weekly summary for {week_start} to {week_end}:")
        # Placeholder for actual logic if data existed
    elif args.clear:
        print("Local data cleared.")
    else:
        print("\nExamples:")
        print('  python healthlog.py --habit "water:250ml"')
        print('  python healthlog.py --symptom "fatigue:mild"')
        print('  python healthlog.py --measure "steps:8432"')
        print('  python healthlog.py --week 1')
        print("Options:")
        print("  -h, --habit      Log a habit")
        print("  -s, --symptom    Record a symptom")
        print("  -m, --measure    Add a measurement")
        print("  -w, --week       Show weekly summary (N)")
        print("  -c, --clear      Clear data")

if __name__ == "__main__":
    print_help()
