# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: HealthLog
class ValidationReport:
    def __init__(self):
        self.warnings = []
        self.errors = []

    def validate_entry(self, entry_type, data):
        if entry_type == 'measurement':
            try:
                float(data.get('value', 0))
            except (TypeError, ValueError):
                self.errors.append(f"Invalid measurement value for {data.get('name')}")
            if data.get('unit') not in ['kg', 'm', 'mmol/L']:
                self.warnings.append(f"Unknown unit '{data.get('unit')}' for {data.get('name')}")
        elif entry_type == 'symptom':
            severity = data.get('severity', '').lower()
            if severity and not severity.startswith(('low', 'moderate', 'high')):
                self.errors.append(f"Invalid symptom severity: '{severity}'")

    def generate_report(self):
        report_lines = ["=== HealthLog Validation Report ===", f"Errors ({len(self.errors)}):\n"]
        for err in self.errors:
            report_lines.append(f"  - {err}")
        if not self.errors and self.warnings:
            report_lines.insert(-1, "Warnings:\n")
        for warn in self.warnings:
            report_lines.append(f"  ! {warn}")
        return "\n".join(report_lines)
