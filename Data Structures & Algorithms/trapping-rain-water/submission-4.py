class Solution:
    def trap(self, h: List[int]) -> int:
        ml = []
        mr = []
        c, d = 0, 0
        for x in h:
            c = max(c, x)
            ml.append(c)
        for x in h[::-1]:
            d = max(d, x)
            mr.append(d)
        mr.reverse()
        minlr = [min(ml[i], mr[i]) for i in range(len(h))]
        return sum([max(minlr[i]-h[i], 0) for i in range(len(h))])

        