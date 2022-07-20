#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random

# 使用链表getRandom无法满足条件
class RandomizedSet:

    def __init__(self):
         self.nums = []
         self.val_idx = {}

    def insert(self, val: int) -> bool:
        if val not in self.val_idx:
            self.nums.append(val)
            self.val_idx[val] = len(self.nums) - 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_idx:
            idx = self.val_idx[val]
            last = self.nums[-1]
            
            self.val_idx[last] = idx
            self.nums[idx] = last
            
            self.nums.pop()
            self.val_idx.pop(val)
            
            return True
        return False

    def getRandom(self) -> int:
        # random 用法
        return self.nums[random.randint(0, len(self.nums)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

