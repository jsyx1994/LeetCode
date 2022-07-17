#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -float("inf"))
        nums.append(-float("inf"))
        
        i = 1
        while i < len(nums) - 1:
            left_ok = nums[i] > nums[i-1]
            right_ok = nums[i] > nums[i+1]
            if left_ok and right_ok:
                return i-1
            i += 1
                
            
# @lc code=end

