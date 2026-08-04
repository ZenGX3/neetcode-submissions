from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [math.prod(nums[:i]) for i in range(len(nums))]
        s = [math.prod(nums[i:]) for i in range(len(nums))]
        l = []
        for i in range(len(nums)):
            l.append(s[i+1] if i == 0 else p[i] if i == len(nums)-1 else s[i+1]*p[i])
        return l

        