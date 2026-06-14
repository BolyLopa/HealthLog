# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: HealthLog
def dry_run_mode():
    import sys, json
    if '--dry-run' in sys.argv:
        print("DRY RUN MODE ENABLED")
        for line in sys.stdin:
            parts = line.strip().split(maxsplit=1)
            cmd, *args = parts
            if cmd == "add_habit":
                name = args[0] if args else ""
                print(f"[SIMULATED] Would add habit: {name}")
            elif cmd == "log_measurement":
                metric = args[0] if args else ""
                value = args[1] if len(args) > 1 else ""
                print(f"[SIMULATED] Would log {metric}: {value}")
            elif cmd == "add_symptom":
                desc = args[0] if args else ""
                severity = args[1] if len(args) > 1 else ""
                print(f"[SIMULATED] Would add symptom: {desc} (severity: {severity})")
            elif cmd == "generate_summary":
                week_start = args[0] if args else "last_week"
                print(f"[SIMULATED] Would generate summary for {week_start}")
            elif cmd == "delete_entry":
                entry_id = args[0] if args else ""
                print(f"[SIMULATED] Would delete entry ID: {entry_id}")
            else:
                print(f"Unknown command in dry-run: {cmd}", file=sys.stderr)
