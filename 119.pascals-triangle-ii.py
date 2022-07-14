#
# @lc app=leetcode id=119 lang=python3 
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last = [1]
        ans = last
        for i in range(rowIndex):
            next_n = len(last)+1
            ans = [0] * next_n
            for j in range(next_n):
                if j == 0 or j == next_n-1:
                    ans[j] = 1
                else:
                    ans[j] = last[j] + last[j-1]
            last = ans
        
        return ans
# @lc code=end

## ********************
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
