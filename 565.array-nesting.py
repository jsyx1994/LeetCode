# @before-stub-for-debug-begin
from python3problem565 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        '''
        数组索引跳转、数组访问记录法
        '''
        i = 0
        _max = -1
        while i < len(nums):
            if nums[i] == -1:
                i += 1
                continue
            
            length = 1
            j = i
            while nums[nums[j]] not in [-1, nums[j]] and nums[j] != -1:
                n_next = nums[j]
                nums[j] = -1
                j = n_next
                length += 1
            
            _max = max(_max, length)
            
            i+=1
        return _max
            
            
# @lc code=end

