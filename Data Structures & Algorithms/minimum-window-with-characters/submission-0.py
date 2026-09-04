class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        cT, w = {}, {}
        for c in t:
            cT[c] = 1 + cT.get(c, 0)
        h, n = 0, len(cT)
        f, fl = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            w[c] = 1 + w.get(c, 0)
            if c in cT and w[c] == cT[c]:
                h += 1
            while h == n:
                if (r - l + 1) < fl:
                    f = [l, r]
                    fl = r - l + 1
                w[s[l]] -= 1
                if s[l] in cT and w[s[l]] < cT[s[l]]:
                    h -= 1
                l += 1
        l, r = f
        return s[l:r+1] if fl != float("inf") else ""
