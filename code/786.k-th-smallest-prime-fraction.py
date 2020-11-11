#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 所有在A[i]/m右边的数字A[j],代表A[i]/A[j]都小于m
        2. 将所有这些数字加起来（cur），可以得到所有A[i]/A[j]<m的数字总和
        3. 当这个数字恰好等于k的时候，找到最大的数字即是答案
    '''
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        l, r, N = 0, 1, len(A)
        while True:
            m = (l + r) / 2
            border = [bisect.bisect(A, A[i] / m) for i in range(N)]
            cur = sum(N - i for i in border)
            if cur > K:
                r = m
            elif cur < K:
                l = m
            else:
                return max([(A[i], A[j]) for i, j in enumerate(border) if j < N], key=lambda x: x[0] / x[1])
# @lc code=end

