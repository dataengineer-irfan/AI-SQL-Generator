import time

from dashboard.performance_tracker import (
    PerformanceTracker
)


tracker = PerformanceTracker()

tracker.start()

tracker.start_generation()
time.sleep(1)
tracker.stop_generation()

tracker.start_execution()
time.sleep(2)
tracker.stop_execution()

tracker.stop()

print()

print(tracker.summary(
    rows=100,
    columns=5
))
