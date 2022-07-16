#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for x in nums:
            if x - 1 not in nums: # 没有经过操作
                y = x + 1
                while y in nums:
                    y += 1
                    
                longest = max(longest, y-x) 
        
        return longest
                    
                
# @lc code=end

