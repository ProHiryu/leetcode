#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        B = sorted(A)
        return B == A or B == A[::-1]
# @lc code=end

