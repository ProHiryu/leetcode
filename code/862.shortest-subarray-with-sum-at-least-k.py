#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = collections.deque([[0, 0]])
        res, cur = float('inf'), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float('inf') else -1
        
# @lc code=end

