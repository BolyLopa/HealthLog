# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: HealthLog
from typing import Optional, List, Dict, Any, Union
import json
from datetime import date, timedelta
from pathlib import Path


def load_config(path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from JSON file with fallback defaults."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"units": {"weight": "kg", "height": "cm"}, "date_format": "%Y-%m-%d"}


def parse_date(date_str: str, fmt: Optional[str] = None) -> date:
    """Parse a date string using config format or fallback."""
    if not fmt:
        fmt = load_config().get("date_format", "%Y-%m-%d")
    try:
        return datetime.strptime(date_str, fmt).date()
    except ValueError as e:
        raise ValueError(f"Invalid date '{date_str}' for format '{fmt}': {e}")


def calculate_week_range(current_date: date) -> tuple[date, date]:
    """Return (start, end) dates of the current week."""
    start = current_date - timedelta(days=current_date.weekday())
    return start, start + timedelta(weeks=1)
