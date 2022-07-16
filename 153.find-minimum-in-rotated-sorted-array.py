#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         ans = 0
#         for i in range(len(nums)- 1):
#             if nums[i+1] < nums[i]:
#                 ans = i+1
#                 break
        
#         return nums[ans]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l + h) // 2
            val = nums[mid]
            
            if val > nums[l]:
                l = mid + 1
            else:
                h = mid - 1
        
        return nums[l]
        
         
        
# @lc code=end

# 二分法
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, h = 0, len(nums)
#         mid = (l + h) // 2
#         while l < h:
#             val = nums[mid]
            
#             if val > nums[l]:
#                 l = mid + 1
#             else:
#                 h = mid - 1
        
#         return nums[l]
