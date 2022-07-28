#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if not nums[i]:
                continue
            
            slow, fast = i,i
            dir = nums[i] > 0
            while nums[slow] or nums[fast]:
                slow = self._next(nums,slow, dir)
                fast = self._next(nums,self._next(nums,fast,dir), dir)
                if slow == -1 or fast == -1:
                    break
                elif slow == fast:
                    return True
                
            slow = i
            while self._next(nums, slow, dir) != -1:
                nums[slow], slow = 0, self._next(nums, slow, dir)
        return False
    
    def _next(self, nums, idx, dir):
        if (nums[idx] > 0) != dir:
            return -1
        next_idx = (idx + nums[idx]) % len(nums)
        
        return -1 if next_idx == idx else next_idx
            
            
# @lc code=end

