# === Stage 16: Add argparse support for the most common commands ===
# Project: HealthLog
import argparse

def main():
    parser = argparse.ArgumentParser(description="HealthLog: Personal wellness log")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Habit command
    habit_parser = subparsers.add_parser('habit', help='Manage habits')
    habit_parser.set_defaults(func=lambda args: print("Habit management not implemented yet"))

    # Measure command
    measure_parser = subparsers.add_parser('measure', help='Record measurements')
    measure_parser.add_argument('--type', required=True, choices=['weight', 'height', 'blood_pressure'], help="Type of measurement")
    measure_parser.set_defaults(func=lambda args: print(f"Recording {args.type}..."))

    # Symptom command
    symptom_parser = subparsers.add_parser('symptom', help='Log symptoms')
    symptom_parser.add_argument('--text', required=True, help="Symptom description")
    symptom_parser.set_defaults(func=lambda args: print(f"Logged: {args.text}"))

    # Summary command
    summary_parser = subparsers.add_parser('summary', help='View weekly summary')
    summary_parser.add_argument('--weeks', type=int, default=1, help="Number of weeks to show")
    summary_parser.set_defaults(func=lambda args: print(f"Summary for last {args.weeks} weeks..."))

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize log file')
    init_parser.set_defaults(func=lambda args: print("Log initialized."))

    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.error(f"Invalid command '{args.command}'")

if __name__ == "__main__":
    main()
