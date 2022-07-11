#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    d = [[1,0],[0,1],[0, -1],[-1,0]]
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        res = False
        for i in range(row):
            for j in range(col):
                res |= self.dfs(board, i,j, word, row, col, 0)
        return res
        
    
    def dfs(self, board, ci, cj, word_left, row, col,p):
        if p >= len(word_left):
            return True
        
        if ci >= row or cj >= col or ci < 0 or cj < 0:
            return False

        if board[ci][cj] != word_left[p]:
            return False
        
        t = board[ci][cj]
        board[ci][cj]=None
        
        ret = False
        for di, dj in self.d:
            x, y = ci+di, cj+dj
            ret |= self.dfs(board,x, y, word_left,row, col,p +1)
        
        board[ci][cj]=t
        return ret 
# @lc code=end

