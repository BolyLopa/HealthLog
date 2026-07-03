# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: HealthLog
import signal
from typing import Optional, Callable


def setup_signal_handlers() -> None:
    """Register graceful shutdown handlers for SIGINT and SIGTERM."""
    def handler(signum: int, frame: Optional[Callable]) -> None:
        print("\n\nHealthLog shutting down gracefully...")
        # Allow cleanup of active threads or file handles here if needed
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)


if __name__ == "__main__":
    setup_signal_handlers()
