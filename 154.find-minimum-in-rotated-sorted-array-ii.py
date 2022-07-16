#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums)-1
        while l < h:
            mid = (l + h) // 2
            # print(l,h)
            if nums[l] < nums[h]:
                return nums[l]
            
            if nums[mid] > nums[h]:
                l = mid + 1
            elif nums[mid] < nums[h]:
                h = mid
            else:
                h -= 1
        
        return nums[l]
# @lc code=end

