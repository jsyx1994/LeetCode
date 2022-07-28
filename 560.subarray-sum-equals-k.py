# @before-stub-for-debug-begin
from python3problem560 import *
from typing import *
from collections import defaultdict
# @before-stub-for-debug-end

#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
#前缀和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = []
        s = 0
        d = {0:1}
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            pre_sum.append(s)
            
            if s - k in d:
                ans += d[s-k]
            
            d[s] = d.get(s, 0) + 1
            # print(d[s])
        return ans           
            
# @lc code=end

