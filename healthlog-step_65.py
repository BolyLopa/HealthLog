# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: HealthLog
import sys, os, re
from pathlib import Path
def merge_imports(src: str) -> str:
    lines = src.splitlines()
    seen = set()
    out = []
    for line in lines:
        if not line.strip(): continue
        m = re.match(r'^\s*import\s+(\S+)', line) or re.match(r'^\s*from\s+\S+\s+import\s+(.+)$', line)
        if m and m.group(1):
            name = m.group(1).split(',')[0].strip()
            if name not in seen:
                out.append(line)
                seen.add(name)
    return '\n'.join(out)
