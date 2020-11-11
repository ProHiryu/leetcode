#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
class Solution:
    '''
    先求出刚好超过K的重复字符串长度，再往前寻找对应的第K个字符
    当当前c为数字时，用N除去对应c，K同时也对N取余，等于在后续位置进行子问题查找
    '''
    def decodeAtIndex(self, S: str, K: int) -> str:
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1
# @lc code=end

