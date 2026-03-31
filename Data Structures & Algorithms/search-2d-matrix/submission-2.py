class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ##3 first do binary search of row 
        ### then binary search of column

        rows = len(matrix)
        cols = len(matrix[0])

        # find row to check
        left, right = 0, len(matrix) -1



        while left < right:
            mid = (left + right) //2
            
            if matrix[mid][0] > target: 
                right = mid - 1
            elif matrix[mid][cols -1] < target:
                left = mid + 1
            else: # in between
                row = mid
                break

        else:
            row = left

        ### now that you have found the row of interest

        left, right = 0, cols - 1 

        while left <= right:
            mid = (left + right) //2
            
            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
        
        return False
