#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        tt = duration
        for i in range(len(timeSeries)-2, -1, -1):
            if timeSeries[i] + duration < timeSeries[i+1]:
                tt += duration
            else:
                tt += timeSeries[i+1] - timeSeries[i]
        
        return tt
# @lc code=end

