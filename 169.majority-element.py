#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        major = nums[0]
        votes = 1
        while i+1 < len(nums):
            i += 1
            if votes == 0:
                major = nums[i]
            
            if nums[i] == major:
                votes += 1
            else:
                votes -= 1
        
        return major
# @lc code=end

