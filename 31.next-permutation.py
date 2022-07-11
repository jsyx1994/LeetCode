#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#


from typing import List
    
'''
1.Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.

2.Find the largest index l > k such that nums[k] < nums[l].

3.Swap nums[k] and nums[l].

4.Reverse the sub-array nums[k + 1:].
'''
# @lc code=start


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        k = n - 1
        while k and nums[k-1] >= nums[k]: # find k = [k + 1]
            k -= 1
        
        if (k <= 0):
            nums.reverse()
            return
            
        l = n - 1 
        while l >= k and nums[k-1] >= nums[l]:
            l -= 1
        
        nums[k-1] , nums[l]  = nums[l], nums[k-1]
        
        j = n - 1
        i = k 
        while j > i:
            nums[i], nums[j] =  nums[j], nums[i]
            j -= 1
            i += 1
        
        
# @lc code=end

