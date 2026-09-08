class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for x in nums:
            i = abs(x)-1
            if nums[i] < 0:
                return abs(x)
            nums[i] = -nums[i]

