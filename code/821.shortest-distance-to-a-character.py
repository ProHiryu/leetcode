#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n, pos = len(S), -float('inf')
        res = [n] * n
        for i in list(range(n)) + list(range(n)[::-1]):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))
        return res

# @lc code=end

