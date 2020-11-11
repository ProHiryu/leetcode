#
# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#

# @lc code=start
class Solution:
    '''
    思路：
        1. O（n）的方法是直接使用遍历循环判断每个数字是否存在s2而不存在s1中
        2. O（logn）的方法是使用选取数字的方法来计算答案
        3. 从N的第一位数字开始，所有小于它的数字都可以取到，如果在s2当中则后面可选取7**(len(N) - i - 1)配合当前数字的good number
        4. 如果在s1当中则相对减掉后面都是s1集合当中数字的情况
        5. 最后记得加上自身是否的一次
    '''
    def rotatedDigits(self, N: int) -> int:
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 8, 2, 5, 6, 9])
        N = [int(d) for d in str(N)]
        s = set()
        res = 0
        for i, d in enumerate(N):
            for j in range(d):
                if s.issubset(s2) and j in s2:
                    res += 7**(len(N) - i - 1)
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)
            if d not in s2:
                return res
            s.add(d)
        return res + (s.issubset(s2) and not s.issubset(s1))
# @lc code=end

