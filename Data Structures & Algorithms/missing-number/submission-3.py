class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        f = len(nums)
        for i, x in enumerate(nums):
            f ^= i ^ x
        return f

        