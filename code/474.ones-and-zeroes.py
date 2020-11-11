#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
class Solution:
    '''
    dp[m][n] = max(dp[m][n], dp[m - x][n - y] + 1)
    '''
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            x, y = s.count('0'), s.count('1')
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
        return dp[m][n]
# @lc code=end

