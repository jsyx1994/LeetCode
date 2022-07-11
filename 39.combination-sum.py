#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from copy import deepcopy
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, candidates: List[int], target: int, path :List[int], result: List[List[int]]):
        if target < 0:
            return
        
        if target == 0:
            result.append(deepcopy(path))
            return
        
        for i in range(len(candidates)):
            path.append(candidates[i])
            self.dfs(candidates[i:], target- candidates[i], path, result)
            path.pop()
        
        
        
# @lc code=end

