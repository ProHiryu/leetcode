#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#

# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1,b1,r1,t1 = rec1
        l2,b2,r2,t2 = rec2
        width = min(r1,r2) - max(l1,l2)
        height = min(t1,t2) - max(b1,b2)
        return width > 0 and height > 0
# @lc code=end

