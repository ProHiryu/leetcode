#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        s //= 2
        dp = [True] + [False for _ in range(s)]
        for n in nums:
            new_dp = [True] + [False for _ in range(s)]
            for i in range(s):
                if n + i > s:
                    break
                new_dp[n + i] = dp[n + i]|(True if dp[i] else False)
                if n + i == s:
                    if new_dp[n + i]:
                        return True
            dp = new_dp
        return dp[s]
# @lc code=end

