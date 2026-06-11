# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: HealthLog
def delete_entry(entry_id, confirm=False):
    if not confirm:
        print(f"Entry {entry_id} will be deleted. Type 'yes' to confirm.")
        return False
    try:
        with open("health_log.txt", "r") as f:
            lines = f.readlines()
        new_lines = []
        for i, line in enumerate(lines):
            parts = line.strip().split("|")
            if len(parts) >= 1 and parts[0] == str(entry_id):
                print(f"Deleted entry {entry_id}.")
            else:
                new_lines.append(line)
        with open("health_log.txt", "w") as f:
            f.writelines(new_lines)
        return True
    except FileNotFoundError:
        print("Log file not found.")
        return False
