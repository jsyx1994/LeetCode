#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for idx, num in enumerate(nums):
            if num in m:
                if abs(m[num] - idx) <= k:
                    return True
            m[num] = idx
        
        return False
# @lc code=end

