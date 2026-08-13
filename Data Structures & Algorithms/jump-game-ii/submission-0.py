class Solution:
    def jump(self, nums: List[int]) -> int:
        f = 0
        c = 0
        nf = 0
        for i in range(len(nums) - 1):
            nf = max(nf, i + nums[i])
            if i == f:
                c += 1
                f = nf
        return c
            