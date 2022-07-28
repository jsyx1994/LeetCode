# @before-stub-for-debug-begin
import itertools
from python3problem566 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
import numpy as np

# class Solution(object):
#     def matrixReshape(self, nums, r, c):
#         try:
#             return np.reshape(nums, (r, c)).tolist()
#         except:
#             return nums

# class Solution(object):
#     def matrixReshape(self, nums, r, c):
#         m = len(nums)
#         n = len(nums[0])
#         if m * n != r * c:
#             return nums
        
#         new_nums = [[0 for _ in range(c)] for _ in range(r)]
#         # print(new_nums)
#         for i in range(r):
#             for j in range(c):
#                 flat_idx = i*c+j
                
#                 new_m = flat_idx // n
#                 new_n = flat_idx % n
#                 # print(new_m, new_n)
#                 new_nums[i][j] = nums[new_m][new_n]
#         return new_nums
# class Solution(object): 
#     def matrixReshape(self, nums, r, c):
#         return nums if len(sum(nums, [])) != r * c else map(list, zip(*([iter(sum(nums, []))]*c)))

# class Solution(object): 
#     def matrixReshape(self, nums, r, c):
#         if r * c != len(nums) * len(nums[0]):
#             return nums
#         it = itertools.chain(*nums)
#         return [list(itertools.islice(it, c)) for _ in range(r)]
        
class Solution(object):  
    def matrixReshape(self, nums, r, c):
        if r * c != len(nums) * len(nums[0]):
            return nums
        else:
            items = [y for x in nums for y in x]
            return [items[x*c : ((x+1)*c)] for x in range(r)]
# @lc code=end

