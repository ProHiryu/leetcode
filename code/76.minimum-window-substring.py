#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = collections.Counter(t)
        count = 0
        l, r = 0, 0
        ans = s + 'a'
        while r < len(s):
            cnt[s[r]] -= 1
            if cnt[s[r]] >= 0:
                count += 1
            while count == len(t):
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                cnt[s[l]] += 1
                if cnt[s[l]] > 0:
                    count -= 1
                l += 1
            r += 1
        return ans if ans != s + 'a' else ''
# @lc code=end

