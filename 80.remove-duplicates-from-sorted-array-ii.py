#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, q = 0,0
        res = 0
        lastp = nums[p]
        count = 0
        while p < len(nums) and q < len(nums):
            if p != q:
                nums[p] = nums[q]
            
            if lastp == nums[p]:
                count+=1
            else:
                lastp = nums[p]
                count =1
                
            if count > 2:
                while q+1 <len(nums) and nums[q] == nums[q+1]:
                    q+=1
                    res+=1
                q+=1
                count = 0
                res+=1
                continue
            
            p+=1
            q+=1
        return len(nums) - res
                
                
            
            
            
# @lc code=end

x= Solution()
x.removeDuplicates([0,0,1,1,1,1,2,3,3])

