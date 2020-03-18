#
# @lc app=leetcode id=686 lang=python3
#
# [686] Repeated String Match
#

# @lc code=start
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        times = -(-len(B) // len(A))
        for i in range(2):
            if B in A*(times + i):
                return times + i
        return -1
# @lc code=end

