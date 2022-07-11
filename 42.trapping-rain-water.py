#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        
        # 指针p、q指向两端
        p, q = 0, len(height)-1
        
        # 分别为p、q扫过最大高度
        lmax, rmax = 0,0
        
        result = 0
        while p < q:
            lmax = max(lmax, height[p])
            rmax = max(rmax, height[q])
            # 当左边扫过最高 小于 右边扫过最高时
            if lmax < rmax:
                result += lmax - height[p] #木桶原理，要么向左夹，要么像右夹
                p += 1 # 左指针向右探索
            else:
                result += rmax - height[q]
                q -= 1
        
        return result
        
# @lc code=end

