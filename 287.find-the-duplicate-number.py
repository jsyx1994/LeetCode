#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # print(nums[i])
            while nums[i] != i+1:
                if nums[i] == nums[nums[i] - 1]:
                    return nums[i]
                
                t = nums[i] -1
                nums[i], nums[t] = nums[t], nums[i]
    
    #Solution 2：two pointers
# @lc code=end

