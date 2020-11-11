#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        d = collections.defaultdict(int)
        for w in A:
            even = ''.join(sorted(w[0::2]))
            odd = ''.join(sorted(w[1::2]))
            d[(even, odd)] += 1
            
        return len(d)
# @lc code=end

