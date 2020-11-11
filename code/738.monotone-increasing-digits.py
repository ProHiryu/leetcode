#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N<10: return N
        A=list(str(N))
        i,n=0,len(A)

        # identify the position when decrease occurs
        while i<n-1 and A[i]<=A[i+1]: i+=1

        # if i==n-1, that means no decrease
        if i==n-1: return N

        # identify the position for equal situation
        while i>0 and A[i]==A[i-1]: i-=1

        # subtract 1 for i and fill the remaining 9
        A[i]=str(int(A[i])-1)
        A[i+1:]=['9']*(n-i-1)

        return int(''.join(A))
# @lc code=end

