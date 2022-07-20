#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
# 使用位运算，[xy]y为下一代，x为上一代
class Solution:
    def gameOfLife(self, board):
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # dead[x0] => live
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board,i,j) == 3:
                        board[i][j] = 2
                        
                # live[x1] => dead
                else: 
                    if self.nnb(board,i,j) < 2 or self.nnb(board,i,j) >3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 1
                if board[i][j] == 3: board[i][j] = 0
                
    def nnb(self, board, i, j):
        '''
        这里对边界的处理需要注意一下
        '''
        m,n = len(board), len(board[0])
        count = 0
        for ii in range(max(i-1, 0), min(i+2, m)):
            for ij in range(max(j-1, 0), min(j+2, n)):
                if (ii == i and ij == j):
                    continue
                count += board[ii][ij] % 2

        
        # if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
        # if i-1 >= 0:                count += board[i-1][j]%2
        # if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
        # if j-1 >= 0:                count += board[i][j-1]%2
        # if j+1 < n:                 count += board[i][j+1]%2
        # if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
        # if i+1 < m:                 count += board[i+1][j]%2
        # if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
        return count
        
        
# @lc code=end
