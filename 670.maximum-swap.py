# @before-stub-for-debug-begin
from python3problem670 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        整数处理
        '''
        s = list(map(int, list(str(num))))
        
        for i in range(len(s) - 1):
            _max = s[i+1]
            _max_idx = i+1
            for j in range(i+2, len(s)):
                if s[j] >= _max:
                    _max = s[j]
                    _max_idx = j
            if _max > s[i]:
                s[i], s[_max_idx] = s[_max_idx], s[i]
                break
        
        s = int(''.join(map(str, s)))
        
        return s
                        
        
# @lc code=end

