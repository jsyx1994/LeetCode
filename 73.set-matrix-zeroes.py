#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #选取第一列为临时存储列，当a【i,j】为0时，
        
        row,col = len(matrix), len(matrix[0])
        clear_row = False
        clear_col = False
        
        for j in range(col):
            if not matrix[-1][j]:
                clear_row = True
        
        for i in range(row):
            if not matrix[i][-1]:
                clear_col = True
        
        for i in range(row-1, -1, -1):
            for j in range(col-1,-1,-1):
                if not matrix[i][j]:
                    matrix[i][-1], matrix[-1][j] = 0, 0
        
        for i in range(0, row-1):
            for j in range(0, col-1):
                if not  matrix[i][-1] or not matrix[-1][j]:
                    matrix[i][j] = 0
                    
        if clear_row:
            for i in range(col):
                matrix[-1][i] = 0
        
        if clear_col:
            for i in range(row):
                matrix[i][-1] = 0
                
# @lc code=end
