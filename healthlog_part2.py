# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: HealthLog
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Measurement:
    value: float
    unit: str
    timestamp: date = field(default_factory=date)

@dataclass
class Symptom:
    name: str
    severity: int  # 1-5
    description: Optional[str] = None
    timestamp: date = field(default_factory=date)

@dataclass
class Habit:
    name: str
    completed: bool = False
    timestamp: date = field(default_factory=date)

@dataclass
class DailyLog:
    date: date
    measurements: List[Measurement] = field(default_factory=list)
    symptoms: List[Symptom] = field(default_factory=list)
    habits: List[Habit] = field(default_factory=list)

@dataclass
class WeeklySummary:
    week_start: date
    week_end: date
    avg_measurements: Optional[float] = None
    symptom_count: int = 0
    completed_habits_count: int = 0
    notes: str = ""
