class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        dp = [ [0] * COLS for r in range(ROWS) ]

        dp[0][0] = 1 # represents starting point. all the possible paths to this point so far

        # fill in first row and first column which only have 1 possible way

        for c in range(1,COLS):
            dp[0][c] = 1
        
        for r in range(1,ROWS):
            dp[r][0] = 1

        # fill in interior
        for r in range(1,ROWS):
            for c in range(1,COLS):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[ROWS-1][COLS-1]