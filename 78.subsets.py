#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        self.dfs(0, len(nums), nums, [], res)
        return res
    
    def dfs(self,start, end, nums, path, res):
        if start >= end:
            res.append(path)
            return
            
        self.dfs(start+1, end, nums, path + [nums[start]], res)
        self.dfs(start+1, end, nums, path, res)
        
        
# @lc code=end

