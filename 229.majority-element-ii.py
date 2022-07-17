#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = len(nums) / 3
        k = float("inf")
        count = 1
        ans = []
        for i in range(0, len(nums)):                
            if nums[i] in ans:
                continue
            
            if nums[i] == k:
                count += 1
            else:
                count = 1
                k = nums[i]
            if count > l:
                ans.append(k)
        return ans
    
    # todo:
# @lc code=end

