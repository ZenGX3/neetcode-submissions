class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            lf, rg = i + 1, len(nums) - 1
            while lf < rg:
                s = a + nums[lf] + nums[rg]
                if s > 0:
                    rg -= 1
                elif s < 0:
                    lf += 1
                else:
                    l.append([a, nums[lf], nums[rg]])
                    lf += 1
                    while nums[lf] == nums[lf - 1] and lf < rg:
                        lf += 1
        return l