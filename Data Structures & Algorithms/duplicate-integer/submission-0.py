class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        return True if sorted(list(set(nums))) != sorted(nums) else False