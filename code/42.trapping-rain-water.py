#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        h_l, h_r = 0, 0
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= h_l:
                    h_l = height[l]
                else:
                    res += min(h_l, height[r]) - height[l]
                l += 1
            else:
                if height[r] >= h_r:
                    h_r = height[r]
                else:
                    res += min(h_r, height[l]) - height[r]
                r -= 1
        return res
                
# @lc code=end

