#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    #Solution 1 : 滑动窗口
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        p, q = 0, 0
        _sum = nums[0]
        min_len = float("inf")
        while p <= q and q < len(nums):
            if _sum < target:  
                q += 1
                if q < len(nums):
                    _sum += nums[q]
            else:
                min_len = min(min_len, q-p + 1)
                _sum -= nums[p]  
                p += 1
        return min_len if min_len != float("inf") else 0
    
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     pass
            
# @lc code=end

