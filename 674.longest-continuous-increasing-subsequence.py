#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0 
        longest = 1
        long = 1
        
        while i < len(nums)-1:            
            if nums[i] < nums[i+1]:
                long += 1
                longest = max(longest, long)    
            else:
                long = 1
            i+=1
        
        return longest
# @lc code=end

