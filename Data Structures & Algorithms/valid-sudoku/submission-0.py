class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in board:
            d = {}
            for y in x:
                if y != ".":
                    d[y] = d.get(y, 0) + 1
            if not all(x == 1 for x in d.values()):
                return False
        
        for i in range(9):
            l = [x[i] for x in board]
            d = {}
            for x in l:
                if x != ".":
                    d[x] = d.get(x, 0) + 1
            if not all(x == 1 for x in d.values()):
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                seen = set()

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] == ".":
                            continue

                        if board[i][j] in seen:
                            return False

                        seen.add(board[i][j])
        return True
        
