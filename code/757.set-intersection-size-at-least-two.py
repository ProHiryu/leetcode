#
# @lc app=leetcode id=757 lang=python3
#
# [757] Set Intersection Size At Least Two
#

# @lc code=start
class Solution:
    '''
    1. 按照结束节点进行排序
    2. 如果之前的区间结束节点在当前开始节点前，则直接加2（取当前区间最大的两个数字，方便和后面进行交集）
    3. 如果两个区间有一个数字相交，只需要加1（取最大的那个数字，即结束节点）
    4. 如果两个区间存在两个以上数字相交，不需要处理
    5. 使用pre保存集合中最后的两个数字（次大和最大的数字），用次大和最大数字和当前区间相比，可以得到上述三种情况
    '''
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1]) # sort by end-point
        ans = 0
        pre = []
        for (s, t) in intervals:
            if not pre or pre[1] < s:
                ans += 2
                pre = [t-1, t]
            elif pre[0] < s:
                pre = [pre[1], t]
                ans += 1
        return ans
# @lc code=end

