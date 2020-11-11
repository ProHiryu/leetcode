#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 计算所有的数字的计数，同时将他们按数字顺序排序
        2. opened代表当前有多少需要满足的数字组合，一开始设置为0
        3. 将待满足的数组情况记录到start这个队列
        4. 如果几个条件达到都可以返回False
        5. O(MlogM + N)
    '''
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        c = collections.Counter(hand)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == W: opened -= start.popleft()
        return opened == 0
# @lc code=end

