class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x in points:
            d = x[0]**2 + x[1]**2
            heapq.heappush(h, (d, x))
        return [heapq.heappop(h)[1] for _ in range(k)]


        