class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = []
        for i in range(len(nums)):
            lf = i + 1
            rg = len(nums) - 1
            while lf < rg:
                s = nums[i] + nums[lf] + nums[rg]
                if s > 0:
                    rg -= 1
                elif s < 0:
                    lf += 1
                else:
                    l.append([nums[i], nums[lf], nums[rg]])
                    lf += 1
                    rg -= 1
        return list(set(map(tuple, l)))
            