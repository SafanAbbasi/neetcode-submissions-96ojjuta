class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}

        def dfs(i,j):

            if i == len(s1) and j == len(s2):
                return i + j == len(s3)

            if i + j >= len(s3):
                return False
            
            if (i,j) in memo:
                return memo[i,j]

            first = False
            second = False
            if i < len(s1) and s1[i] == s3[i+j]:
                first = dfs(i+1, j)
            if j < len(s2) and s2[j] == s3[i+j]:
                second = dfs(i, j+1)
            memo[(i,j)] = first or second

            return memo[(i,j)] 


        return dfs(0,0)