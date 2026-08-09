class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r, c = len(m), len(m[0])
        rz = False
        for i in range(r):
            for j in range(c):
                if m[i][j] == 0:
                    m[0][j] = 0
                    if i > 0:
                        m[i][0] = 0
                    else:
                        rz = True
        for i in range(1, r):
            for j in range(1, c):
                if m[0][j] == 0 or m[i][0] == 0:
                    m[i][j] = 0
        
        if m[0][0] == 0:
            for i in range(r):
                m[i][0] = 0

        if rz == True:
            for j in range(c):
                m[0][j] = 0

