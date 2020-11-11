#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        cnt = collections.Counter((A + ' ' + B).split(' '))
        return [w for w, c in cnt.items() if c == 1]
# @lc code=end

