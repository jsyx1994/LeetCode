#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, jump = 0, 0
        while i < len(nums):
            #jump to see if has new zeros
            while i + jump < len(nums) and nums[i + jump] == 0:
                jump += 1
            
            jumps = i + jump
            #if nums[i] = 0
            if jumps < len(nums) and nums[i] == 0:
                nums[i], nums[jumps] = nums[jumps], nums[i]                
            
            i += 1
        
        return nums
    
    #Solution 2 : two pointers
# @lc code=end

