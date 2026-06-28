# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: HealthLog
def calculate_weekly_score(records):
    score = 0
    for r in records:
        if r.get('type') == 'habit':
            score += r.get('value', 1) * 2
        elif r.get('type') == 'measurement':
            target = r.get('target_value', 70)
            actual = r.get('value', 0)
            if isinstance(actual, (int, float)) and isinstance(target, (int, float)):
                score += max(0, 1 - abs(actual - target) / target) * 5
        elif r.get('type') == 'symptom':
            severity = r.get('severity', 3)
            if severity < 2:
                score -= severity
    return min(score, 100)

def get_priority_recommendation(records):
    issues = []
    for r in records:
        if r.get('type') == 'measurement':
            target = r.get('target_value', 70)
            actual = r.get('value', 0)
            if isinstance(actual, (int, float)) and isinstance(target, (int, float)):
                diff = abs(actual - target) / max(1, target) * 100
                if diff > 20:
                    issues.append(f"Check {r.get('name', 'measurement')}: value is {actual}, target is {target}")
        elif r.get('type') == 'symptom':
            severity = r.get('severity', 3)
            if severity >= 3:
                issues.append(f"Address symptom '{r.get('name', 'unknown')}': severity level {severity}")
    return sorted(issues, key=lambda x: len(x))[:5]
