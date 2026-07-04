# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: HealthLog
class HealthLogMessages:
    """Centralized user-facing strings for consistent UI and logs."""
    
    WELCOME = "Welcome to HealthLog! Track your habits, measurements, and symptoms."
    HABIT_ADDED = "Habit '{name}' added successfully. Keep it up!"
    MEASUREMENT_LOGGED = f"Logged {metric} value: {value:.2f}"
    SYMPTOM_NOTED = "Symptom noted for today. Remember to rest if needed."
    
    WEEK_SUMMARY_HEADER = "Weekly Wellness Summary"
    WEEK_SUMMARY_HABITS = "Habits Completed This Week:"
    WEEK_SUMMARY_METRICS = "Average Measurements:"
    WEEK_SUMMARY_SYMPTOMS = "Common Symptoms Reported:"
    
    ERROR_INVALID_DATE = "Please enter a valid date (YYYY-MM-DD)."
    ERROR_EMPTY_VALUE = "Measurement value cannot be empty."
    ERROR_DUPLICATE_HABIT = "Habit '{name}' already exists for this day."
    
    EXAMPLE_ENTRY = """Example Entry:
  Date: 2023-10-27
  Habits: ['Drink Water', 'Meditate']
  Measurements: {'Weight': 68.5, 'SleepHours': 7.2}
  Symptoms: []"""
