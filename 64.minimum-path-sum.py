#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from xmlrpc.client import MAXINT


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dij = grid
        
        for i in range(m):
            for j in range(n):

                left = dij[i-1][j] if i -1 >=0 else MAXINT
                top  = dij[i][j-1] if j-1 >=0 else MAXINT
                if left == top == MAXINT:
                    continue
                
                dij[i][j] += min(left, top)
        
        # print(dij)
        return dij[-1][-1]
# @lc code=end

