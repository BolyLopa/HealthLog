# === Stage 57: Add structured result objects for command handlers ===
# Project: HealthLog
class Result(BaseModel):
    success: bool
    message: str = ""
    data: Optional[Any] = None
    error: Optional[str] = None

def handle_add_habit(command: dict) -> Result:
    if not command.get("name"):
        return Result(success=False, message="Missing habit name")
    new_habit = Habit(name=command["name"], streak=0)
    repo.habits.append(new_habit)
    return Result(success=True, message=f"Habit '{new_habit.name}' added", data=new_habit)

def handle_get_summary(command: dict) -> Result:
    week_start = datetime.now() - timedelta(weeks=1)
    weekly_data = {"habits": [], "measurements": []}
    for h in repo.habits:
        if h.last_log and h.last_log.date().date() >= week_start.date():
            weekly_data["habits"].append({"name": h.name, "streak": h.streak})
    return Result(success=True, message="Weekly summary generated", data=weekly_data)
