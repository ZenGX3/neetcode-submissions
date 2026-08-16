class MedianFinder:

    def __init__(self):
        self.hl, self.hr = [], []
        heapq.heapify_max(self.hl)
        heapq.heapify(self.hr)

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.hl, num)

        if self.hl and self.hr and self.hl[0] > self.hr[0]:
            val = heapq.heappop_max(self.hl)
            heapq.heappush(self.hr, val)

        if len(self.hl) > len(self.hr) + 1:
            val = heapq.heappop_max(self.hl)
            heapq.heappush(self.hr, val)

        if len(self.hl) + 1 < len(self.hr):
            val = heapq.heappop(self.hr)
            heapq.heappush_max(self.hl, val)

    def findMedian(self) -> float:
        if len(self.hl) > len(self.hr):
            return self.hl[0]

        if len(self.hr) > len(self.hl):
            return self.hr[0]

        return (self.hl[0] + self.hr[0]) / 2