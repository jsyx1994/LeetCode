# @before-stub-for-debug-begin
from python3problem665 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        chance_used = False
        x1 = nums[:]
        x2 = nums[:]
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                if not chance_used:
                    chance_used = True
                    
                    x1[i+1] = nums[i]
                    x2[i] = nums[i+1]
                else:
                    return False
        
        x1_ans = True
        x2_ans = True
        for i in range(len(x1)-1):
            if x1[i+1] < x1[i]:
                x1_ans = False
                break
        
        for i in range(len(x2)-1):
            if x2[i+1] < x2[i]:
                x2_ans = False
                break
        return x1_ans or x2_ans
                
# @lc code=end

