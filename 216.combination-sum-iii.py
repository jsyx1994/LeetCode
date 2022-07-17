#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(k, n, [], [], ans ,1)
        return ans
    
    def dfs(self, k, target, chosens:List, path: List, ans : List,now):
        if k < 0 or target < 0:
            return
        
        if target == 0 and k == 0:
            ans.append(path)
        
        for i in range(now, 10):
            if i not in chosens:
                self.dfs(k-1, target-i, chosens + [i] , path + [i], ans, i)
            
# @lc code=end

