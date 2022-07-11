#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #insert
        if not intervals:
            return [newInterval]
        
        is_insert = False
        for i in range(len(intervals)):
            
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                is_insert = True
                break
        
        if not is_insert:
            
            intervals.append(newInterval)
         
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
print(x.insert([[1,5]], [2,7]))