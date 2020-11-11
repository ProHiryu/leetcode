#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mi, ma = min(A), max(A)
        return 0 if ma - mi - 2*K <= 0 else ma - mi - 2*K
# @lc code=end

