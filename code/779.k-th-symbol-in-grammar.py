#
# @lc app=leetcode id=779 lang=python3
#
# [779] K-th Symbol in Grammar
#

# @lc code=start
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return bin(K - 1).count('1') & 1
# @lc code=end

