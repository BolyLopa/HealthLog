# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: HealthLog
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {h['cmd']: h for h in handlers}

    def dispatch(self, text):
        cmd = text.strip().lower()
        if cmd not in self.handlers:
            print("Unknown command.")
            return False
        handler = self.handlers[cmd]
        args = [a.strip() for a in text.split(maxsplit=1)[1].split()]
        try:
            result = handler['func'](*args)
            if callable(result):
                print(result())
            else:
                print(result)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def register(self, cmd, func):
        self.handlers[cmd.strip().lower()] = {'func': func}
