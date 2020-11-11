#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cnt = Counter(T)
        res = ''
        for c in S:
            res += cnt[c] * c
            del(cnt[c])
        for c, t in cnt.items():
            res += t*c
        return res
# @lc code=end

