#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        
        nums[:len(nums)-k] = list(reversed(nums[:len(nums)-k]))
        nums[-k:] = list(reversed(nums[-k:]))
        nums.reverse()
        
# @lc code=end

