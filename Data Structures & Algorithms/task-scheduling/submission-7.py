class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        hM = [x for x in c.values()]
        heapq.heapify_max(hM)
        t = 0
        q = deque()
        while hM or q:
            t += 1
            if q and q[0][1] <= t:
                heapq.heappush_max(hM, q.popleft()[0])
            if hM:
                ct = heapq.heappop_max(hM) - 1
                if ct:
                    q.append([ct, t+n+1])
        return t



