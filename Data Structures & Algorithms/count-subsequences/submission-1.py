class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # m, n = len(s), len(t)

        # dp = [0] * ( n+1) # 1D DP for space optim

        # dp[0] = 1

        # for i in range(1, m+1):

        #     for j in range(n,0, -1):
        #         if s[i-1] == t[j-1]:
        #             dp[j] += dp[j-1]
        

        # return dp[n]


        cache = {}

        n, m = len(s), len(t)

        def dfs(i, j):
            
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i,j)] = ( dfs(i+1,j+1) + dfs(i+1, j))
            else:
                cache[(i,j)] = dfs(i+1, j)

            return cache[(i,j)]

        return dfs(0,0)