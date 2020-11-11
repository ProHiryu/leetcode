#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        for s, e in intervals:
            if not res:
                res.append([s, e])
                continue
            if s <= res[-1][1]:
                res[-1][1] = max(res[-1][1], e)
            else:
                res.append([s, e])
        return res
# @lc code=end

