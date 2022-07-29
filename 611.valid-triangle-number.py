#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         '''
#         TLE
#         '''
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     if nums[i] + nums[j] > nums[k] and abs(nums[i]-nums[j]) < nums[k]:
#                         ans += 1
#         return ans
    
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         count=0
#         for i in range(len(nums)-2):
#             k = i+2
#             for j in range(i+1,len(nums)-1):
#                 if nums[i] == 0:
#                     continue
#                 while k < len(nums) and nums[i]+nums[j] > nums[k]:
#                     k+=1
                
#                 count += k - j - 1
#         return count
    
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        三指针、三和
        '''
        nums.sort()
        count=0
        for i in range(len(nums)-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count
                
# @lc code=end

