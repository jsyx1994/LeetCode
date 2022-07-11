#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from functools import reduce
from typing import List
from xmlrpc.client import MAXINT


class Solution:
    def jump(self, nums: List[int]) -> int:
        d = [-1] * len(nums)
        return self.dp(0, len(nums), nums, d)
        
    def dp(self, k, n, nums, d):
        if k >= n-1:
            return 0
        if d[k]!=-1:
            return d[k]
        
        # print( k, n)
        d[k] = 1 + reduce(min, [self.dp(i, n, nums, d) for i in range(k+1, k+ nums[k] + 1) ], MAXINT)
        return d[k]
        
# @lc code=end

x = Solution()
print(x.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]))

