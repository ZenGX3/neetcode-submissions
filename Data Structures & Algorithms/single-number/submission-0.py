class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = 0
        for x in nums:
            f ^= x
        return f