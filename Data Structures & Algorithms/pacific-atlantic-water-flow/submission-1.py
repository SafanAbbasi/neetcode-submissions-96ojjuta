class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # feels like a dfs question.
        rows, cols = len(heights), len(heights[0])

        directions = [ (1,0), (-1,0), (0,1), (0,-1)]

        islands = []

        pacificset = set()
        atlanticset = set()

        def dfs(r,c, visited, prev_height):
            
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or heights[r][c] < prev_height:
                return

            visited.add((r,c))

            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])


            

        # Pacific: top row and left column
        for c in range(cols):
            dfs(0, c, pacificset, -1)        # top row
        for r in range(rows):
            dfs(r, 0, pacificset, -1)        # left column

        # Atlantic: bottom row and right column
        for c in range(cols):
            dfs(rows - 1, c, atlanticset, -1)  # bottom row
        for r in range(rows):
            dfs(r, cols - 1, atlanticset, -1)  # right column

        res = []
        for r in range(rows):
            for c in range(cols):  
                if (r,c) in pacificset and (r,c) in atlanticset:
                    res.append([r,c])

        return res