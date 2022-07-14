#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        self.dfs(0, len(nums), nums, [], res)
        return res
    
    def dfs(self,start, end, nums, path, res):
        if start >= end:
            if path not in res:
                res.append(path)
            return
            
        self.dfs(start+1, end, nums, path + [nums[start]], res)
        self.dfs(start+1, end, nums, path, res)
        
# @lc code=end

