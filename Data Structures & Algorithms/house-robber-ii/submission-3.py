class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.hrob1(nums[1:]), self.hrob1(nums[:-1]))
    def hrob1(self, nums):
        r1, r2 = 0, 0
        for x in nums:
            new = max(r1 + x, r2)
            r1 = r2
            r2 = new
        return r2
