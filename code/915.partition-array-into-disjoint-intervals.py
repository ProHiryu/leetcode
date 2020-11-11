#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        cur = 0
        minn = min(cnt.keys())
        for i in range(len(A)):
            cur = max(cur, A[i])
            cnt[A[i]] -= 1
            if cnt[A[i]] == 0:
                del cnt[A[i]]
                if minn == A[i]:
                    minn = min(cnt.keys())
            if minn >= cur:
                return i + 1
            
# @lc code=end

