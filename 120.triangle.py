#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from xmlrpc.client import MAXINT


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1] if j > 0 else MAXINT , triangle[i-1][j] if j< len(triangle[i-1]) else MAXINT)
        return min(triangle[-1])
            
        
# @lc code=end

