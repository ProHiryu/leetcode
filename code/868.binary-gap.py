#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)
        res = 0
        i = float('inf')
        for j, n in enumerate(s[2:]):
            if n == '1':
                res = max(res, j - i)
                i = j
        return res
# @lc code=end

