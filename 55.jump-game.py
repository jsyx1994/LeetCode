#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= curr:
                curr = i
                
        return not curr
# @lc code=end