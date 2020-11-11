#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
    
        def match(word, pattern):
            if len(word) != len(pattern):
                return False
            d = {}
            for w, p in zip(word, pattern):
                if w not in d:
                    if p in d.values():
                        return False
                    d[w] = p
                else:
                    if d[w] != p:
                        return False
            return True
                    
        for w in words:
            if match(w, pattern):
                res.append(w)
        return res
# @lc code=end

