#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = 0, len(nums)-1
        
        ret = -1
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                ret = mid
                break
            
            if nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                  
                continue  
                    
            if nums[mid] >= nums[low]:
                if nums[mid] > target  >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1 
                
                continue
        
        if ret == -1:
            return [-1,-1]
        
        
        x = ret
        y = ret
        while x+1 < len(nums):
            if nums[x+1] == target:
                x += 1
            else:
                break
                
        while y-1 >= 0:
            if nums[y-1] == target:
                y -= 1
            else:
                break
        
        return [y, x]
# @lc code=end

