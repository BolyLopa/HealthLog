# === Stage 32: Add pagination helpers for long console output ===
# Project: HealthLog
def paginate_output(text, max_lines=15):
    """Yields chunks of text limited by line count."""
    lines = text.splitlines()
    for i in range(0, len(lines), max_lines):
        yield '\n'.join(lines[i:i+max_lines]) + ("\n..." if i + max_lines < len(lines) else "")

def print_paginated(text, max_lines=15):
    """Prints text with pagination markers."""
    for chunk in paginate_output(text, max_lines):
        print(chunk)
