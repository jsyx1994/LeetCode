#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key= lambda x: x[0])  
        # print(intervals)      
        i = 1

        while i < len(intervals):
            now = intervals[i]
            last = intervals[i-1]
            
            if now[0] <= last[1]:
                last[1] = max(now[1],last[1])
                intervals.pop(i)
            else:
                i += 1
        return intervals
            
        
# @lc code=end

x = Solution()
print(x.merge([[1,4],[0,4]]))
