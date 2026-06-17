# === Stage 27: Add monthly summary calculations ===
# Project: HealthLog
def calculate_monthly_summary(records):
    from collections import defaultdict
    monthly_data = defaultdict(lambda: {"habits": [], "measurements": [], "symptoms": []})
    for record in records:
        month_key = f"{record['date'][:7]}"  # YYYY-MM
        if record.get("habit"):
            monthly_data[month_key]["habits"].append(record["habit"])
        elif record.get("measurement"):
            monthly_data[month_key]["measurements"].append({"type": record["measurement"], "value": record["value"]})
        elif record.get("symptom"):
            monthly_data[month_key]["symptoms"].append(record["symptom"])

    summary = []
    for month, data in sorted(monthly_data.items()):
        habit_counts = defaultdict(int)
        for h in data["habits"]:
            habit_counts[h] += 1
        measurement_types = {}
        for m in data["measurements"]:
            t = m["type"]
            if t not in measurement_types:
                measurement_types[t] = []
            measurement_types[t].append(m["value"])

        symptom_list = data["symptoms"]
        summary.append({
            "month": month,
            "top_habits": dict(sorted(habit_counts.items(), key=lambda x: x[1], reverse=True)[:3]),
            "measurements_summary": {k: {"avg": sum(v)/len(v) if v else 0, "min": min(v), "max": max(v)} for k, v in measurement_types.items()},
            "symptoms_count": len(symptom_list)
        })

    return summary
