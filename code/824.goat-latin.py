#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set(['a','e','i','o','u','A','E','I','O','U'])
        res = []
        for i, w in enumerate(S.split()):
            if w[0] in vowel:
                res.append(w + 'ma' + (i+1) * 'a')
            else:
                res.append(w[1:] + w[0] + 'ma' + (i+1)*'a')
        return ' '.join(res)
# @lc code=end

