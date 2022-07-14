#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums : List[int], target: int) -> bool:

        low, high = 0, len(nums)-1
        
        while low <= high:
            
            #去重
            while low<high and nums[low] == nums[low+1]:
                low+=1
            while low<high and nums[high] == nums[high-1]:
                high-=1
            
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return True
                        
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
            
        return False
        
# @lc code=end

