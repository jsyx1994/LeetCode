#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            if  mid + 1 < n and nums[mid] < target < nums[mid + 1]:
                return mid + 1
            
            if mid -1 >=0 and nums[mid - 1] < target < nums[mid]:
                return mid
            
            
            if nums[mid] < target:
                low = mid + 1
            
            if nums[mid] > target:
                high = mid - 1
                
        return low
            
# @lc code=end

