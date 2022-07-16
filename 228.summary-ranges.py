#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i += 1
            res.append("{0}->{1}".format(start, nums[i]) if start != nums[i] else "{0}".format(nums[i]))
            i+=1
        return res
# @lc code=end

