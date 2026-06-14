# === Stage 19: Add undo support for the last simple mutation ===
# Project: HealthLog
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

class HealthLog:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.current_state: Dict[str, Any] = {}

    def _save_snapshot(self) -> None:
        snapshot = {
            "state": json.dumps(self.current_state),
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(snapshot)

    def set_measurement(self, key: str, value: float) -> None:
        if len(self.history) > 10:
            self.history.pop(0)
        self._save_snapshot()
        self.current_state[key] = value

    def undo_last_change(self) -> Optional[float]:
        if not self.history:
            return None
        
        last_snapshot = self.history[-1]
        try:
            old_value = json.loads(last_snapshot["state"])[key]
            del self.history[-1]
            self.current_state.update(json.loads(last_snapshot["state"]))
            return old_value
        except (KeyError, ValueError):
            return None

    def get_current(self) -> Dict[str, Any]:
        return dict(self.current_state)
