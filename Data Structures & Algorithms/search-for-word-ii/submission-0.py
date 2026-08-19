class Node:
    def __init__(self):
        self.chld = {}
        self.eow = False
    
    def addw(self, word):
        cur = self
        for c in word:
            if c not in cur.chld:
                cur.chld[c] = Node()
            cur = cur.chld[c]
        cur.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rt = Node()
        for wd in words:
            rt.addw(wd)
        
        rw, cl = len(board), len(board[0])
        f, v = set(), set()
        def dfs(r, c, nd, wd):
            if r < 0 or c < 0 or r == rw or c == cl or (r, c) in v or board[r][c] not in nd.chld:
                return
            v.add((r, c))
            nd = nd.chld[board[r][c]]
            wd += board[r][c]

            if nd.eow:
                f.add(wd)
            dfs(r + 1, c, nd, wd)
            dfs(r - 1, c, nd, wd)
            dfs(r , c + 1, nd, wd)
            dfs(r, c - 1, nd, wd)
            v.remove((r, c))
        for i in range(rw):
            for j in range(cl):
                dfs(i, j, rt, "")
        return list(f)
        