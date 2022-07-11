#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = m -1
        print(m//2)
        for i in range(m):
            for j in range(i+1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        for i in range((m)):
            for j in range(m//2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
        
        # print(matrix[::-1])
        # print(*matrix[::-1])
        # print(*zip(*matrix[::-1]))
        
        # matrix[:] = zip(*matrix[::-1]) #注意python的方法
        
# @lc code=end

x = Solution()
y = [[1,2,3],[4,5,6],[7,8,9]]
x.rotate(y)
print(y)