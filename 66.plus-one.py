#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1
        i, c = 0 , 0
        while i < len(digits):
            if c:
                digits[i] += 1
                c=0
            
            if digits[i] >= 10:
                digits[i] = digits[i]-10
                c= 1
            i += 1
        
        if c:
            digits.append(1)
            
            
        return digits[::-1]            
                

# @lc code=end

