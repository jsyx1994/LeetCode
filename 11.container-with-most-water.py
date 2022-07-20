#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    """跨度与两根中最短的乘积最大
    """
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        
        while i < j:
            max_area = max(max_area, (j-i) * min(height[i] , height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
# @lc code=end

