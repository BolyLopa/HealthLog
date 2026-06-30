# === Stage 66: Add export of a short status dashboard ===
# Project: HealthLog
def export_dashboard(data, output_file="dashboard.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("HEALTH LOG DASHBOARD\n")
        f.write("=" * 40 + "\n\n")
        
        habits = data.get("habits", {})
        if habits:
            f.write("HABITS STATUS:\n")
            for name, status in habits.items():
                symbol = "✓" if status else "✗"
                f.write(f"{symbol} {name}\n")
            f.write("\n")
        
        measurements = data.get("measurements", [])
        if measurements:
            f.write("RECENT MEASUREMENTS:\n")
            for item in measurements[-5:]:
                key, value = list(item.items())
                f.write(f"{key}: {value}\n")
            f.write("\n")
        
        symptoms = data.get("symptoms", [])
        if symptoms:
            f.write("RECENT SYMPTOMS:\n")
            for item in symptoms[-5:]:
                key, value = list(item.items())
                f.write(f"{key}: {value}\n")
            f.write("\n")
        
        weekly_summary = data.get("weekly_summary", {})
        if weekly_summary:
            f.write("WEEKLY SUMMARY:\n")
            for key, val in weekly_summary.items():
                f.write(f"- {val}\n")
            f.write("=" * 40 + "\n")
