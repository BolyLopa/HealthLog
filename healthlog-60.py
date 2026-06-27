# === Stage 60: Add saved views for frequently used filters ===
# Project: HealthLog
class SavedViewManager:
    def __init__(self, db):
        self.db = db
        self.views = {}

    def save_view(self, name, filters=None, sort_by='date', order='desc'):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("View name must be a non-empty string.")
        view_data = {
            'name': name,
            'filters': filters or {},
            'sort_by': sort_by,
            'order': order
        }
        self.views[name] = view_data
        return True

    def load_view(self, name):
        if name not in self.views:
            raise KeyError(f"Saved view '{name}' does not exist.")
        return self.views[name].copy()

    def list_views(self):
        return list(self.views.keys())
