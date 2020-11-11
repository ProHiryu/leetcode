#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return zip(*A)
# @lc code=end

