#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    #Solution 1:置换
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     for i in range(len(nums)):
    #         while nums[i] != i + 1:
    #             t = nums[i] - 1
    #             if nums[i] == nums[t]:
    #                 break
    #             nums[i], nums[t] = nums[t], nums[i]
            
        
    #     ret = []
    #     for i in range(len(nums)):
    #         if nums[i] != i + 1:
    #             ret.append(i+1)
    #     return ret
    
    #Solution 2: 
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            t = abs(nums[i]) - 1
            nums[t] = - abs(nums[t])
            
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
# @lc code=end

