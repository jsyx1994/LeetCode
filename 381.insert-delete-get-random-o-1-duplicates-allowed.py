#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
import random
class RandomizedCollection:

    def __init__(self):
         self.nums = []
         self.val_idx = {}

    def insert(self, val: int) -> bool:

        self.nums.append(val)
        if val not in self.val_idx:
            self.val_idx[val] = [len(self.nums) - 1]
            ret = True
        else:
            self.val_idx[val].append(len(self.nums) - 1)
            ret = False
        
        # print(self.nums, self.val_idx)
        return ret

    def remove(self, val: int) -> bool:
        if val in self.val_idx:
            idx = self.val_idx[val].pop() # 随便取一
            last = self.nums[-1]                  
            self.nums[idx] = last  
            if last in self.val_idx:
                self.val_idx[last].append(idx)
                if len(self.nums) - 1 in self.val_idx[last]:
                    self.val_idx[last].remove(len(self.nums) - 1)
            
            if not self.val_idx[val]:
                self.val_idx.pop(val)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        # random 用法
        return random.choice(self.nums)

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

