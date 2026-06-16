# === Stage 24: Add grouped summaries by category or status ===
# Project: HealthLog
def generate_grouped_summary(records, group_by='category'):
    from collections import defaultdict
    groups = defaultdict(list)
    for r in records:
        key = r.get(group_by, 'Other') or 'Unknown'
        groups[key].append(r)
    summary_lines = []
    for name, items in sorted(groups.items()):
        if not items: continue
        values = [str(i.get('value', '')) for i in items]
        statuses = set(i.get('status', '') for i in items)
        status_str = ' | '.join(sorted(statuses)) if len(statuses) > 1 else (statuses.pop() or '')
        summary_lines.append(f"[{name}] {len(items)} entries: values={values} [{status_str}]")
    return '\n'.join(summary_lines)
