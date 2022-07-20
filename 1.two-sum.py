#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
            
        for i, num in enumerate(nums):
            if (target - num) in d.keys():
                return [i, d[target-num]]
            d[num] = i
        
# @lc code=end

