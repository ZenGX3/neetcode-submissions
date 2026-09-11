class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        while r > l:
            r = r&(r-1)
        return r