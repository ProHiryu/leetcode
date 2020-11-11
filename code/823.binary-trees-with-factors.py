#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
class Solution:
    '''
    1. bottom-up dp solution
    2. every answer is the product of each sub_set answer
    3. if k and n//k are both in the dp set, we can add answers
    4. sort of A is to gureentee bottom-up solution correct
    '''
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = dict()
        for n in sorted(A):
            dp[n] = sum(dp[k] * dp.get(n//k, 0) for k in dp if n % k == 0) + 1
        return sum(dp.values()) % (10**9 + 7)
# @lc code=end

