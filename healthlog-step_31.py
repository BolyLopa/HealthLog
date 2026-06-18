# === Stage 31: Add compact table rendering for long lists ===
# Project: HealthLog
def render_compact_table(data, columns=None):
    if not data: return ""
    if columns is None: columns = list(data[0].keys())
    header = "  |".join(columns) + "\n"
    separator = "-+-".join(["-" * (len(c) + 2) for c in columns]) + "\n"
    rows = []
    for row in data[:15]:
        r = "  |".join(str(row.get(col, "")) for col in columns)
        if len(r) > 60:
            lines = [r[i:i+20] for i in range(0, len(r), 20)]
            rows.append("  |\n    ".join(lines))
        else:
            rows.append(r)
    return header + separator + "\n".join(rows[:15])
