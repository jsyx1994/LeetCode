#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        if n <=0:
            return True
        while i < len(flowerbed):            
            if not flowerbed[i] and \
            ((i+1 < len(flowerbed) and not flowerbed[i+1]) or (i+1 >= len(flowerbed))) and \
            ((i-1>=0 and not flowerbed[i-1]) or (i-1 < 0)):
                # flowerbed[i] = 1  
                n-=1
                i+=2
                if n <=0:
                    return True
                
                continue
            i+=1
        # print(flowerbed)
        return False
                
# @lc code=end

