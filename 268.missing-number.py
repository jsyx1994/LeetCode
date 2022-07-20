#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(1, len(nums) + 1)) - sum(nums)
# @lc code=end

