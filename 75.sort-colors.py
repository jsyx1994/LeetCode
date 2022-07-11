#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start[0,1,0]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p, q = 0, len(nums)-1
        i = 0
        while i <= q:
            
            while nums[i] == 2 and i < q:
                nums[i],  nums[q] = nums[q], nums[i]
                q -= 1
            while nums[i] == 0 and i > p:
                nums[i],  nums[p] = nums[p], nums[i]
                p+=1
            i += 1
            # print(nums, p, q, i)
            
# @lc code=end
