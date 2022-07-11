#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_h  =0, len(matrix)
        
        while row_l < row_h:
            tar_row = (row_l + row_h ) //2
            if matrix[tar_row][0] > target:
                row_h -= 1
                continue
            
            if matrix[tar_row][-1] < target:
                row_l += 1
                continue
            
            if  matrix[tar_row][0] <= target <= matrix[tar_row][-1]:
                l, h = 0, len(matrix[tar_row])
                
                while l < h:
                    mid = (l + h) //2
                    
                    if matrix[tar_row][mid] == target:
                        return True
                    
                    elif matrix[tar_row][mid] > target:
                        h -= 1
                    elif matrix[tar_row][mid] < target:
                        l += 1
                
                return False
        
        return False
                    
# @lc code=end

