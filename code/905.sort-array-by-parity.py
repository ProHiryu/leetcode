#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            while i < len(A) - 1 and A[i] % 2 == 0:
                i += 1
            while j > 0 and A[j] % 2 == 1:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
        return A
# @lc code=end

