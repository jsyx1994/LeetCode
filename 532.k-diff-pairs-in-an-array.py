#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] and k !=0 :
                continue
            if self.b_search(nums, i+1, len(nums)-1, nums[i] + k):
                ans.add(nums[i])
        
        return len(ans)
                
    def b_search(self,nums, low, high, target) -> bool:
        while low <= high:
            mid = (high - low) //2 + low
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
# @lc code=end

