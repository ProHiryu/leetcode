#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        l = 0
        for r in range(len(A)):
            if K >= 0:
                res = max(res, r - l)
            if A[r]: continue
            K -= 1
            while K < 0:
                while A[l]: l += 1
                K += 1
                l += 1
        if K >= 0: res = max(res, r - l + 1)
        return res
# @lc code=end

