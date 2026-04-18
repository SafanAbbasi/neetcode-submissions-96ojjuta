from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                cr, cc = queue.popleft()

                for dr, dc in directions: # delta row and delta columns
                    nr, nc = cr + dr, cc + dc 
                    if 0 <= nr < rows and 0 <= nc < cols: # check if new row and col are in bounds
                        if (nr,nc) not in visited and grid[nr][nc] == '1':
                            visited.add((nr, nc))
                            queue.append((nr,nc))



#        outer logic that calls bfs(r, c) goes here. flood all connected island parts when you find a 1
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    count += 1
                    bfs(r, c)    # marks entire island as visited

        return count