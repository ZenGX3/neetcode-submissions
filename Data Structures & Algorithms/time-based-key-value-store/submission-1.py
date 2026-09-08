class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        v = self.d.get(key, [])
        l = 0
        r = len(v) - 1
        f = ""
        while l <= r:
            m = (l + r)//2
            if v[m][1] <= timestamp:
                f = v[m][0]
                l = m + 1
            else:
                r = m - 1
        return f
