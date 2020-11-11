#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 数学证明：
            x + (x+1) + (x+2)+...+ k terms = N
            kx + k*(k-1)/2 = N
            kx = N - k*(k-1)/2
        2. 存在这种x即可，x就是起始位置
    '''
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        for k in range(2, int(sqrt(2*N)) + 1):
            if (N - k*(k - 1)//2) % k == 0:
                res += 1
        return res
# @lc code=end

