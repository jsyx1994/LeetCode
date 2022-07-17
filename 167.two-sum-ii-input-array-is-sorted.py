#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    #Solution 1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            t = target - numbers[i]
            if t in d:
                return [d[t], i + 1]
            else:
                d[numbers[i]] = i + 1
    
    #Solution 2
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for idx, n in  enumerate(numbers):
    #         t = target - n
    #         ans = Solution.b_search(numbers, t, idx + 1, len(numbers)-1)
    #         # print(n, target-n, ans)
    #         if ans is not None:
    #             return [idx + 1, ans + 1]
            
    # @staticmethod
    # def b_search(nums : List[int], target, l, h):
    #     while l <= h:
    #         mid = (h-l)//2 + l
    #         if nums[mid] == target:
    #             return mid
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             h = mid - 1
                
    #     return None
# @lc code=end

