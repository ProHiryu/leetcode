#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i + len(s):] if S[i:i + len(s)] == s else S
        return S
# @lc code=end

