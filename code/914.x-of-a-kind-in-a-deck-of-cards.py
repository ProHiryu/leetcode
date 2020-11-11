#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        res = 0
        for i in count:
            res = gcd(i, res)
        return res > 1
# @lc code=end

