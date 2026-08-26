class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        r, c = len(grid), len(grid[0])
        v = set()
        ilds = 0
        def bfs(x, y):
            q = collections.deque()
            v.add((x, y))
            q.append((x, y))
            while q:
                row, col = q.popleft()
                dirn = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dirn:
                    x, y = row + dr, col + dc
                    if x in range(r) and y in range(c) and grid[x][y] == "1" and (x, y) not in v:
                        q.append((x, y))
                        v.add((x, y))
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in v:
                    bfs(i, j)
                    ilds += 1
        return ilds
