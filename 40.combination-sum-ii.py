#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort() # 关键
        self.dfs(candidates, target, [], ret, 0)
        
        return ret
    
    def dfs(self, candidates: List[int], target: int, path :List[int], result: List[List[int]], start):
        if target < 0:
            return
        
        if target == 0:
            result.append(path)
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]: #关键
                continue
            
            self.dfs(candidates, target- candidates[i], path + [candidates[i]], result, i + 1)
# @lc code=end

