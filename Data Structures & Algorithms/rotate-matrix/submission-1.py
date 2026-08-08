class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n = len(m)

        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                m[i][j], m[j][n-1-i], m[n-1-i][n-1-j], m[n-1-j][i] = \
                m[n-1-j][i], m[i][j], m[j][n-1-i], m[n-1-i][n-1-j]