#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
          
        for i in range(n):
            while(nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]):
                #注意python无内置swap，无法值交换，面试可写伪代码
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp - 1] = tmp

        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
            
        return n+1
        
            
# @lc code=end