class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        ls = []
        l, r = 0, len(m[0])
        t, b = 0, len(m)
        while l < r and t < b:
            for i in range(l, r):
                ls.append(m[t][i])
            t += 1
            for i in range(t, b):
                ls.append(m[i][r-1])
            r -= 1

            if not (l < r and t < b):
                break
            for i in range(r-1, l-1, -1):
                ls.append(m[b-1][i])
            b -= 1
            for i in range(b-1, t-1, -1):
                ls.append(m[i][l])
            l += 1
        return ls
                