class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # you have to know which 3x3 you are in 
        # for each cell, if its not empty, check 
            # 1. vertical, horizontal, and in 3x3 box
            # check that cell value does not repeat anywhere in those 3 domains
            # how to know which 3x3 we are in?
            
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # do we check a 3x3 square at a time or each cell sequentially and keep track of which square we are in?
        for r in range(9):

            for c in range(9):
                square = 3 * (r // 3) + c // 3

                if board[r][c] != ".":
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                    if board[r][c] in boxes[square]:
                        return False
                    else:
                        boxes[square].add(board[r][c])

        return True


### Solution with HashMap

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         rows = [defaultdict(int) for _ in range(9)]
#         cols = [defaultdict(int) for _ in range(9)]
#         boxes = [defaultdict(int) for _ in range(9)]

#         for r in range(9):
#             for c in range(9):
#                 val = board[r][c]
#                 if val == ".":
#                     continue

#                 square = 3 * (r // 3) + c // 3

#                 rows[r][val] += 1
#                 cols[c][val] += 1
#                 boxes[square][val] += 1

#                 if rows[r][val] > 1 or cols[c][val] > 1 or boxes[square][val] > 1:
#                     return False

#         return True