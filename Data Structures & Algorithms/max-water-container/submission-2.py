class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h)-1
        ma = 0
        while r > l:
            ma = max(ma, min(h[l], h[r])*(r - l))
            l, r = (l + 1, r) if h[l] < h[r] else (l, r - 1)
        return ma

