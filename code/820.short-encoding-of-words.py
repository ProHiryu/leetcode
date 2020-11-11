#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return len(s) + sum([len(w) for w in s])
# @lc code=end

