#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dij = [[0] *n for _ in range(m)]
        dij[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i -1 >=0:
                    dij[i][j] += dij[i-1][j]
                
                if j-1 >=0:
                    dij[i][j] += dij[i][j-1]
                    
        return dij[-1][-1]
                    
# @lc code=end

