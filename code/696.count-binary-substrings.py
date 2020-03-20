#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l=[]
        for i in s.replace("01","0 1").replace("10","1 0").split():
            l.append(len(i))
        return sum(min(a,b) for a,b in zip(l,l[1:]))
# @lc code=end

