class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # maximum elevation along the way is minimized.

        directions = [[1,0],[-1,0], [0,1],[0,-1]]

        minheap = []

        ROWS, COLS = len(grid), len(grid[0])

        minheap = [(grid[0][0], 0, 0)]  # (elevation, row, col)

        visited = set()
        visited.add((0,0)) # starting point
        

        while minheap:
            elevation , cr, cc = heapq.heappop(minheap)

            if cr == ROWS -1 and cc == COLS-1:
                return elevation
            for dr,dc in directions:
                nr , nc = dr+cr, dc + cc
                if 0 <= (nr) < ROWS and 0<= (nc) < COLS and (nr,nc) not in visited:
                    heapq.heappush(minheap, (max(elevation, grid[nr][nc]), nr, nc))
                    visited.add((nr,nc))

            

