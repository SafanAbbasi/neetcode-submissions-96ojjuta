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


        ### Optimized solution
        row = [1] * n  # base case: first row is all 1s

        for i in range(m - 1):
            newRow = [1] * n   # first column is always 1
            for j in range(1, n):
                newRow[j] = newRow[j - 1] + row[j]
            row = newRow

        return row[n - 1]

        ### Shorter code

        # dp = [[0] * COLS for r in range(ROWS)]
        # dp[0][0] = 1

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if r == 0 and c == 0:
        #             continue
        #         top  = dp[r-1][c] if r > 0 else 0
        #         left = dp[r][c-1] if c > 0 else 0
        #         dp[r][c] = top + left

        # return dp[ROWS-1][COLS-1]