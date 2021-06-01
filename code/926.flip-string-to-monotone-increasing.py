#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        res = zeros = s.count("0")
        for c in s:
            ones, zeros = (ones + 1, zeros) if c == "1" else (ones, zeros - 1)
            res = min(res, ones + zeros)
        return res
# @lc code=end

