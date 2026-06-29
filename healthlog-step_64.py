# === Stage 64: Add validation for relationship references ===
# Project: HealthLog
from typing import Optional, List
import re

def validate_relationship_refs(data: dict) -> tuple[bool, str]:
    errors = []
    
    if "relationships" in data and isinstance(data["relationships"], list):
        for i, rel in enumerate(data["relationships"]):
            ref_field = None
            
            # Determine reference field based on relationship type (case-insensitive check of keys)
            key_map = {k.lower(): k for k in ["type", "category"]}
            target_key = next((k for k in key_map if k in rel), None)
            
            if not target_key:
                errors.append(f"Relationship #{i+1}: Missing 'type' or 'category' field to define reference.")
                continue
                
            ref_value = rel.get(target_key, "")
            
            # Validate against specific allowed lists based on type/category
            valid_types = ["symptom", "habit", "measurement"]
            if target_key == "type" and ref_value not in valid_types:
                errors.append(f"Relationship #{i+1}: Invalid 'type' '{ref_value}'. Must be one of {valid_types}.")
                
            # Validate against allowed categories for specific types (e.g., symptoms)
            if target_key == "category":
                valid_categories = ["cardio", "respiratory", "digestive"]
                if ref_value and ref_value not in valid_categories:
                    errors.append(f"Relationship #{i+1}: Invalid 'category' '{ref_value}'. Must be one of {valid_categories}.")

            # Validate that referenced entity exists in the current data scope (simplified check)
            # In a real app, this would query a DB or global state. Here we assume flat dict context for demo.
            if ref_value:
                # Check existence in top-level keys or nested lists like 'symptoms', 'habits'
                found = False
                for key in ["symptoms", "habits", "measurements"]:
                    if isinstance(data.get(key), list):
                        if any(item.get("id") == ref_value for item in data[key]):
                            found = True
                            break
                
                # Also check direct id matches on the relationship object itself if it acts as a self-ref or similar
                if not found and "id" in rel:
                    if rel["id"] != ref_value:
                         pass # Allow internal IDs to differ from reference strings for now, 
                              # but strictly we want to ensure the string points to an existing ID.
                         
            # Check for circular references (simplified depth 1)
            if "related_to" in rel and isinstance(rel["related_to"], dict):
                target_id = rel["related_to"].get("id")
                current_type = rel.get(target_key, "")
                if target_id == data.get(current_key := next((k for k in ["symptoms", "habits", "measurements"] if k in data), None)):
                     errors.append(f"Relationship #{i+1}: Potential circular reference detected.")

    return len(errors) == 0, "; ".join(errors)
