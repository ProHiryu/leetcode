#
# @lc app=leetcode id=1234 lang=python3
#
# [1234] Replace the Substring for Balanced String
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = collections.Counter(s)
        res = n = len(s)
        l = 0
        for r, c in enumerate(s):
            cnt[c] -= 1
            while l < n and all(n//4 >= cnt[c] for c in 'QWER'):
                res = min(r - l + 1, res)
                cnt[s[l]] += 1
                l += 1
        return res
# @lc code=end

