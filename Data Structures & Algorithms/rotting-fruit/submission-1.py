class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this feels like bfs problem
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # each layer is like a minute
        # all the surrounding rotten fruits need to expand their rottingness at the same time

        # find all initally rotten fruits

        # 
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))

        minutes = 0
        while q:
            added = False
            for _ in range(len(q)):

                r,c = q.popleft()

                for dr, dc in directions:
                    nr , nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        added = True
        
            if added:
                minutes += 1

        ### do I have to check after the bfs queue logic if there are any fresh fruit still existing with a double for loop? 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return minutes