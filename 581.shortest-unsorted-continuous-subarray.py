#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        双指针、重复数字处理
        '''
        i, j = 0, len(nums)-1
        
        while i < j:
            if nums[j-1] <= nums[j] and j-1 >= 0:
                j -= 1
                continue
            
            if nums[i+1] >= nums[i] and i < len(nums)-1:
                i += 1
                continue
            break
        
        temp = nums[i:j+1]
        _min = min(temp)
        _max = max(temp)
        while i > 0 and _min < nums[i-1]:
            i -= 1
        
        while j < len(nums) - 1 and _max > nums[j+1]:
            j += 1 
        
        return j-i + 1 if j>i else 0
        
# @lc code=end

