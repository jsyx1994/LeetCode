#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #The meaning of return a and b is that when a is empty, the function jumps out. When a is not empty, b is executed. I am confused about this.
        return  matrix and [*matrix.pop(0)] + self.spiralOrder(list(zip(*matrix))[::-1])
# @lc code=end

