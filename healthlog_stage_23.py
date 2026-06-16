# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: HealthLog
def manage_tags(tags, item):
    if tags is None:
        return {}
    new_tags = set(item.get("tags", []))
    for tag in list(new_tags):
        if tag.startswith("#"):
            continue
        if tag not in tags:
            tags[tag] = 0
        tags[tag] += 1

def remove_tag(tags, item):
    if tags is None or "tags" not in item:
        return {}
    new_tags = set(item.get("tags", []))
    for tag in list(new_tags):
        if tag.startswith("#"):
            continue
        if tag in tags and tags[tag] > 0:
            tags[tag] -= 1
            if tags[tag] == 0:
                del tags[tag]

def get_tag_summary(tags, limit=5):
    if not tags:
        return []
    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    result = [{"tag": tag, "count": count} for tag, count in sorted_tags[:limit]]
    return result
