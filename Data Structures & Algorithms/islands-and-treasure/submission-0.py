from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [ (-1,0), (1,0), (0,1), (0,-1)]

        INF = (2**31) -1
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            cr , cc = queue.popleft() 
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[cr][cc] + 1
                    queue.append((nr, nc)) 