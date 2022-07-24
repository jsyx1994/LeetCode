#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
            if len(s) <= 3:
                continue
            
            min_ = min(s)
            s.remove(min_)
        # print(s)
        return min(s) if len(s) >= 3 else max(s)
# @lc code=end

