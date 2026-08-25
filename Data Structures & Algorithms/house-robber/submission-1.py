class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for x in nums:
            tmp = max(x + r1, r2)
            r1 = r2
            r2 = tmp
        return r2