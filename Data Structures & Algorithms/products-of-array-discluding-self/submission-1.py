from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            l.append(math.prod(temp))
        return l

        