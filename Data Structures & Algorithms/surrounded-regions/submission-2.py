class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find 0's and then determine if they are all surrounded by X's on all four sides
        # Phase 1: Walk the border. For every 'O' on an edge, DFS and mark it as safe.
        # Phase 2: Walk the entire grid. Every 'O' that wasn't marked safe → flip to 'X'.
        # Phase 3: Every safe cell → flip back to 'O'.

        rows, cols = len(board), len(board[0])
        directions = [ (1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r,c):


            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            board[r][c] = 'S'
            
            for dr, dc in directions:
                dfs(r + dr, c + dc)



        for r in range(rows):
            dfs(r,0)
        
        for c in range(cols):
            dfs(0,c)

        for r in range(rows):
            dfs(r,cols-1)
        
        for c in range(cols):
            dfs(rows-1,c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
                if board[r][c] == 'S':
                    board[r][c] = "O"
