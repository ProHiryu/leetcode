#
# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#

# @lc code=start
class Solution:
    '''
     (1) 先对原始序列排序（排序是不影响结果的哦，这个很好理解）
    （2）现在单独分析一个排序后的元素A[i]，那么这个元素在所有子集中，有几次是被作为最大值的？又有几次是被作为最小值的？
    （3）继续分析，很显然A[i]被作为最大值的次数为 2^i - 1次（这里i从0开始），如何理解？0 ~ i 的所有子集共有2^(i+1)种，又因为每一位又两种状态，所以取最后一位被选中的有 2^i种，再减去只取这一位的1种，所以最后只有2^i - 1 。
    （4）继续分析，很显然A[i]被作为最小的次数为 2^(n - i - 1) - 1次（这里i从0开始，n为数列的长度），倒过来分析，此时的i为最低位。
    '''
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        n, res, mod = len(A), 0, 10**9 + 7
        pow2 = [1]
        for i in range(1, n):  # 先把2的次方求好
            pow2.append(pow2[-1] * 2 % mod)

        for i, x in enumerate(A):
            res += (pow2[i] - 1) * x  # x 被作为最大值得 次数 应该加上
            res -= (pow2[n-1-i] - 1) * x  # x 被作为最小值得 次数 应该减去
            res %= mod
        return res
# @lc code=end

