#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dij = [[0] *n for _ in range(m)]
        dij[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dij[i][j] = 0
                    continue
                
                if i -1 >=0:
                    dij[i][j] += dij[i-1][j]
                
                if j-1 >=0:
                    dij[i][j] += dij[i][j-1]
        
        # print(dij)
        return dij[-1][-1]
# @lc code=end

