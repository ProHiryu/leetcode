#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        def Most(S):
            if S < 0: return 0
            res = l = 0
            for r in range(len(A)):
                S -= A[r]
                while S < 0:
                    S += A[l]
                    l += 1
                res += r - l + 1
            return res
        return Most(S) - Most(S - 1)
# @lc code=end

