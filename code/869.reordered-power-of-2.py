#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]
# @lc code=end

