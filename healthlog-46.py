# === Stage 46: Add a schema version field and migration helper ===
# Project: HealthLog
SCHEMA_VERSION = "1.1"

def migrate_data(data: dict) -> dict:
    if data.get("schema_version") != SCHEMA_VERSION:
        old_v = data.get("schema_version", "0.9")
        if old_v == "0.9":
            for habit in data.get("habits", []):
                if not isinstance(habit, dict) or "name" not in habit:
                    continue
                habit["completed_at"] = None
                data.setdefault("schema_version", SCHEMA_VERSION)
        elif old_v == "0.8":
            for sym in data.get("symptoms", []):
                if isinstance(sym, str):
                    data["symptoms"].append({"name": sym, "severity": 1})
                    data["symptoms"] = [s for s in data["symptoms"] if not isinstance(s, str)]
        else:
            raise ValueError(f"Unsupported schema version: {old_v}")
    return data

def ensure_schema_version(data: dict) -> None:
    if "schema_version" not in data:
        data["schema_version"] = SCHEMA_VERSION
