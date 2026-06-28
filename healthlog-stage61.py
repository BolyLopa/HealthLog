# === Stage 61: Add performance timing for core list and search operations ===
# Project: HealthLog
import time
from functools import wraps
from typing import Callable, Any

def timed(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] took {end - start:.4f}s")
        return result
    return wrapper

def benchmark_list_ops(data: list[str], threshold_ms: float = 10.0):
    iterations = max(1, int((threshold_ms / (time.perf_counter() - time.perf_counter())) * 0.5))
    if iterations < 3: iterations = 3
    
    # Warm-up
    _ = data.index("x") if "x" in data else None
    
    start = time.perf_counter()
    for i in range(iterations):
        idx = data.index(data[i % len(data)])
        found = data.count(data[i % len(data)])
        exists = "target" in data
    end = time.perf_counter()
    
    print(f"[List Ops] {iterations} iters: index={end - start:.4f}s, avg={(end-start)/iterations*1000:.2f}ms")

def benchmark_search_ops(data: list[str], query: str) -> dict[str, float]:
    start = time.perf_counter()
    
    # Linear search simulation (common in small logs)
    linear_time = 0.0
    for item in data:
        if item.startswith(query):
            break
    
    # Count occurrences
    count_time = 0.0
    cnt = 0
    for _ in range(len(data)):
        if query in data[_]:
            cnt += 1
    
    end = time.perf_counter()
    
    return {
        "linear_search_ms": (end - start) * 1000,
        "count_occurrences_ms": ((end - start) / len(data)) * 1000 if data else 0.0,
        "found_count": cnt
    }

# Usage example integration:
# @timed
# def get_weekly_summary(log_data): ...
# benchmark_list_ops(self.habits_log)
