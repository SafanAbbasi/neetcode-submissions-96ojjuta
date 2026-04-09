class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # you have to know which 3x3 you are in 
        # for each cell, if its not empty, check 
            # 1. vertical, horizontal, and in 3x3 box
            # check that cell value does not repeat anywhere in those 3 domains
            # how to know which 3x3 we are in?

        ROWS, COLS = len(board), len(board[0]) - 1 
        square = 1 
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # do we check a 3x3 square at a time or each cell sequentially and keep track of which square we are in?
        for r in range(ROWS):

            for c in range(COLS):
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


                    # if board[r][c] in board[0:r][c] or board[r][c] in board[r+1:][c]: # check vertical
                    #     return False
                    # if board[r][c] in board[r][0:c] or board[r][c] in board[r][c+1:]: # chec horizontal
                    #     return False
                    # if board[r][c] in board[]