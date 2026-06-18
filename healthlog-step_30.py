# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: HealthLog
def parse_date(date_str: str, formats=None) -> datetime.date | None:
    """Parse a date string using common formats and return a date object."""
    if formats is None:
        formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d.%m.%Y"]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: {', '.join(formats)}")

def normalize_date_input(user_input: str) -> tuple[datetime.date, list[str]]:
    """Parse user input and return the parsed date along with a list of unused format strings."""
    try:
        parsed = parse_date(user_input)
        used_formats = [f for f in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"] if f"{parsed.year}-{parsed.month:02d}-{parsed.day:02d}".startswith(f.replace("%", ""))]
        return parsed, []
    except ValueError as e:
        print(f"Error: {e}")
        return None, ["%Y-%m-%d", "%d/%m/%Y"]
