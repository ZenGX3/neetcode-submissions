class Solution:
    def trap(self, h: List[int]) -> int:
        ml = [max(h[:i+1]) for i in range(len(h))]
        mr = [max(h[i:]) for i in range(len(h))]
        minlr = [min(ml[i], mr[i]) for i in range(len(h))]
        return sum([max(minlr[i]-h[i], 0) for i in range(len(h))])

        