#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mi, ma = ans, ans
        for i in range(1, len(nums)):
            # print(mi, ma)
            n = nums[i]
            if n < 0:
                mi, ma = ma, mi
                
            ma = max(n, ma * n)
            mi = min(n, mi * n)
            ans = max(ma, ans)
            
        return ans
            
        
        
# @lc code=end

