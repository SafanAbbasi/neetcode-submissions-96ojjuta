from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxarea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(r,c) -> int:

            queue = deque()
            queue.append((r,c))
            
            grid[r][c] = 0
            area = 1

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 0
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxarea = max(maxarea, bfs(r,c))


        return maxarea

        # maxarea = 0
        # rows, cols = len(grid), len(grid[0])
        # directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # def dfs(r,c) -> int:

        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
        #         return 0
            
        #     grid[r][c] = 0
        #     area = 1


        #     for dr, dc in directions:
        #         area += dfs( r + dr, c + dc)
            
        #     return area

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             island_area = dfs(r,c)
        #             maxarea = max(maxarea, island_area)


        # return maxarea