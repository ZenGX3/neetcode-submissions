class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(max(nums)):
            if i not in nums:
                return i
        return max(nums) + 1

        