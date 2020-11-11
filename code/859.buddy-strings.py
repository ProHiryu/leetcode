#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) <= 1 or len(B) <= 1 or len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) < len(A)
        i = 0
        while A[i] == B[i]: i += 1
        for j in range(i + 1, len(A)):
            if A[j] == B[i] and A[i] == B[j]:
                A = A[:i] + A[j] + A[i+1:j] + A[i] + A[j+1:]
        return A == B
# @lc code=end

