#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows+1):
            ans = [0] * i
            for j in range(i):
                # print(i,j)
                # print(res)
                if j == 0 or j == i - 1:
                    ans[j] = 1
                else:
                    ans[j] = res[i-2][j-1] + res[i-2][j]
            res.append(ans)
            
        return res
                
            
# @lc code=end

