#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.dp(triangle, 0, len(triangle) - 1)[0]
        
    def dp(self, triangle, depth, m):
        if depth == m:
            return triangle[depth]
        last = self.dp(triangle, depth + 1, m)
        res = []
        for i, n in enumerate(triangle[depth]):
            res.append(n + min(last[i], last[i + 1]))
        return res

# @lc code=end

