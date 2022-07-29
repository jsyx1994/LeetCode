#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        s = sum(nums[:k])
        i, j = 0, k-1
        max_sum = s
        while j+1 < len(nums) and i+1<len(nums):
            i+=1
            j+=1
            s += nums[j] - nums[i-1]
            max_sum = max(max_sum, s)
        return max_sum / k 
# @lc code=end

