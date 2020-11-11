#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#

# @lc code=start
class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(p, 3))
# @lc code=end

