#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        g, l = -float("inf"), -float("inf")
        for n in nums:
            l = max(n, l + n)
            g = max(g, l)
        return g
# @lc code=end

