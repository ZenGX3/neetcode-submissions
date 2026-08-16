class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        a = 0
        for i in range(k):
            a = heapq.heappop_max(nums)
        return a