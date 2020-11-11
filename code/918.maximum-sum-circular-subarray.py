#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        minl, ming, maxl, maxg = float("inf"), float("inf"), float("-inf"), float("-inf")
        for n in A:
            minl = min(n, n + minl)
            ming = min(ming, minl)
            maxl = max(n, n + maxl)
            maxg = max(maxg, maxl)
        return max(maxg, sum(A) - ming) if maxg > 0 else maxg
# @lc code=end

