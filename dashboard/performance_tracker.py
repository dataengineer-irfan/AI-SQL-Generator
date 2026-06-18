import time


class PerformanceTracker:

    def __init__(self):
        self.start_time = None
        self.generation_start = None
        self.execution_start = None

        self.generation_time = 0
        self.execution_time = 0
        self.total_time = 0

    def start(self):
        self.start_time = time.perf_counter()

    def start_generation(self):
        self.generation_start = time.perf_counter()

    def stop_generation(self):
        self.generation_time = (
            time.perf_counter()
            - self.generation_start
        )

    def start_execution(self):
        self.execution_start = time.perf_counter()

    def stop_execution(self):
        self.execution_time = (
            time.perf_counter()
            - self.execution_start
        )

    def stop(self):
        self.total_time = (
            time.perf_counter()
            - self.start_time
        )

    def summary(
        self,
        rows=0,
        columns=0
    ): 
        return {
            "generation_time": round(
                self.generation_time,
                3
            ),
            "execution_time": round(
                self.execution_time,
                3
            ),
            "total_time": round(
                self.total_time,
                3
            ),
            "rows": rows,
            "columns": columns
        }
