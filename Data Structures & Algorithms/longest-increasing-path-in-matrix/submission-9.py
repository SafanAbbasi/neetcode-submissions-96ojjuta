# import sys
# sys.setrecursionlimit(10000)
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

#         directions = [(0,1), (0,-1), (1,0), (-1,0)]
#         ROWS, COLS = len(matrix), len(matrix[0])
#         memo = {}

#         def dfs(r,c):

#             if (r,c) in memo:
#                 return memo[(r,c)]

#             distance = 1
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc

#                 if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
#                     distance = max(distance, 1 + dfs(nr, nc))

#             memo[(r, c)] = distance
#             return distance


#         maxlength = 0 

#         for r in range(ROWS): 
#             for c in range(COLS):
#                 maxlength = max(maxlength, dfs(r,c))
        
#         return maxlength 

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())

