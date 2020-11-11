#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    '''
    dp[stone + i] = max(dp[stone + i], dp[i] + stone)
    '''
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        m = s // 2

        dp = [0 for _ in range(m + 1)]
        for stone in stones:
            for i in range(m + 1, -1, -1):
                if stone + i <= m:
                    dp[stone + i] = max(dp[stone + i], dp[i] + stone)
        return s - 2*(dp[-1])
# @lc code=end

