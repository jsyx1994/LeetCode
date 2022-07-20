#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = set()
        for i in range(len(nums)):
            while nums[i] != i + 1:
                t = nums[i] - 1
                if nums[i] == nums[t]:
                    ret.add(nums[i])
                    break
                    
                nums[i] , nums[t] = nums[t], nums[i]
        return list(ret)
                
# @lc code=end

