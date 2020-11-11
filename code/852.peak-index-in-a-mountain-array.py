#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A) - 1
        while l < r:
            m = (l + r) // 2
            if A[m] < A[m+1]:
                l = m + 1
            else:
                r = m
        return l
# @lc code=end

