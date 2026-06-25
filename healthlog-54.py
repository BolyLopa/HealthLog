# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: HealthLog
def colorize(text, style=""):
    codes = {"reset": "\033[0m", "bold": "\033[1m", "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m"}
    if not style: return text
    prefix = codes.get(style, "")
    suffix = codes["reset"]
    return f"{prefix}{text}{suffix}"

def print_header(title):
    print(colorize(f"\n=== {title} ===", "bold"))

def print_success(msg):
    print(colorize(f"✓ {msg}", "green"))

def print_warning(msg):
    print(colorize(f"⚠ {msg}", "yellow"))

def print_error(msg):
    print(colorize(f"✗ {msg}", "red"))
