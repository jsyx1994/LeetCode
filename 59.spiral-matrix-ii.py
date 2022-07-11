#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[0] *n for _ in range(n)]
        
        i,j ,di,dj = 0,0,0,1
        
        for k in range(n*n):
            ret[i][j] = k +1
            if ret[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i+=di
            j+=dj
        return ret
# @lc code=end


x = Solution()
x.generateMatrix(4)
