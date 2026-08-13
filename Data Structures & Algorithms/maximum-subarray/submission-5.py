class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c = nums[0]
        a = nums[0]
        for x in nums[1:]:
            c = max(x, c+x)
            a = max(a, c)
        return a