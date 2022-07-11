#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from functools import reduce
from typing import List
from xmlrpc.client import MININT


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsi = MININT
        si = MININT
        for ai in nums:
            if si <=0 :
                si = ai
            else:
                si += ai
            
            maxsi = max(si, maxsi)         
        
        return maxsi
        
    #python本身较慢，分治算法会超时
    def dac(self, m, n, nums):
        if m > n :
            return MININT
         
        mid = n + m//2
        
        rmax, lmax = 0, 0
        
        for i in range(mid+1, n):
            s += nums[i]
            rmax = max(rmax, s)
            
        s = 0
        for i in range(mid-1, m-1, -1):
            s += nums[i]
            lmax = max(lmax, s)
            
        ldac = self.dac(m,mid-1,nums)
        rdac = self.dac(mid + 1,n,nums)
        
        # print(ldac, rdac, lmax + rmax + nums[mid], nums[mid], mid)
        
        return max(ldac, rdac, lmax + rmax + nums[mid])
# @lc code=end

x= Solution()
print(x.maxSubArray([5,4,-1,7,8]))