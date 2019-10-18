import tracemalloc


class TraceMemory:
    def __init__(self, top=10, key_type="lineno"):
        self.top = top
        self.key_type = key_type

    def __call__(self, func):
        """监控内存消耗情况
        """
        def wrapper(*args, **kwgs):
            tracemalloc.start()
            result = func(*args, *kwgs)
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics(self.key_type)
            for info in top_stats[:self.top]:
                print("memory info:", info)
            return result
        return wrapper