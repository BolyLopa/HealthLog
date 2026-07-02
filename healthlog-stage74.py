# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: HealthLog
def compare_snapshots(before: dict, after: dict) -> str:
    """Generate a compact text diff between two state snapshots."""
    lines = ["=== HealthLog Snapshot Comparison ===", f"Date Before: {before.get('date', 'N/A')}", f"Date After:  {after.get('date', 'N/A')}"]
    
    for key in before.keys():
        val_before = before.get(key, "None")
        val_after = after.get(key, "None")
        
        if isinstance(val_before, list) and isinstance(val_after, list):
            lines.append(f"\n[{key}] (Lists):")
            common_keys = set(val_before).intersection(set(val_after))
            added = sorted(set(val_after) - set(val_before))
            removed = sorted(set(val_before) - set(val_after))
            
            if added:
                lines.append(f"  + Added: {added}")
            if removed:
                lines.append(f"  - Removed: {removed}")
            if common_keys:
                lines.append(f"  ~ Unchanged count: {len(common_keys)}")
        elif val_before != val_after:
            status = "↑" if (val_after > val_before) else ("↓" if (val_after < val_before) else "≠")
            lines.append(f"\n[{key}]: {status}")
            lines.append(f"  Before: {val_before}")
            lines.append(f"  After:  {val_after}")
        else:
            lines.append(f"[{key}] (Unchanged)")
    
    return "\n".join(lines)
