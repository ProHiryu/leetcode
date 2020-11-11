#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = collections.Counter()
        for b in B:
            c = collections.Counter(b)
            for i, x in c.items():
                cnt[i] = max(x, cnt[i])

        res = []
        for a in A:
            c = collections.Counter(a)
            if all(c[i] >= cnt[i] for i in cnt.keys()):
                res.append(a)
        return res
# @lc code=end

