#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    direction = [(0,1),(-1,0),(0,-1),(1,0)]
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.dfs(grid, i, j)
                # print(area)
                max_area = max(area, max_area)
            
        return max_area
                    
    def dfs(self, grid, i, j):
        if i<0 or i>= len(grid) or j<0 or j>=len(grid[0]) or not grid[i][j]:
            return 0
        else:
            grid[i][j] = 0
            # print(i,j)
            area = 1 #注意
            for d in self.direction:
                n_i, n_j = i + d[0], j + d[1]
                area += self.dfs(grid, n_i, n_j)
            
            return area
            
# @lc code=end

