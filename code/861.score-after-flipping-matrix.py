#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 思路很简单，首先第一位数字必须要为1，因为其他后面的收益必定加起来都不会超过第一位是1的收益
        2. 从每一列看，只要得到1的数目即可，和0的数目求个最大值就是每一列能够得到的最大收益
    '''
    def matrixScore(self, A: List[List[int]]) -> int:
        M, N = len(A), len(A[0])
        res = (1 << N - 1) * M
        for j in range(1, N):
            cur = sum(A[i][j] == A[i][0] for i in range(M))
            res += max(cur, M - cur) * (1 << N - 1 - j)
        return res
# @lc code=end

