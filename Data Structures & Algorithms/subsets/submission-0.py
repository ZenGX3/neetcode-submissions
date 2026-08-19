class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        f = []
        s = []
        def dfs(ind):
            if ind >= len(nums):
                f.append(s.copy())
                return
            s.append(nums[ind])
            dfs(ind + 1)

            s.pop()
            dfs(ind + 1)
        dfs(0)
        return f