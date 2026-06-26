# === Stage 56: Add compact error classes for domain failures ===
# Project: HealthLog
class HealthLogError(Exception): pass
class HabitNotMet(HealthLogError): pass
class MeasurementOutOfBounds(HealthLogError): pass
class SymptomMismatch(HealthLogError): pass
class SummaryGenerationFailed(HealthLogError): pass
class DataCorrupted(HealthLogError): pass
class InvalidDateRange(HealthLogError): pass
class DuplicateEntryFound(HealthLogError): pass
