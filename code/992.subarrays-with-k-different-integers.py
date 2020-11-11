#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def k_most(k):
            count = 0
            l, r = 0, 0
            cnt = collections.Counter()
            while r < len(A):
                cnt[A[r]] += 1
                while len(cnt) > k:
                    cnt[A[l]] -= 1
                    if cnt[A[l]] == 0:
                        del cnt[A[l]]
                    l += 1
                count += r - l + 1  
                r += 1
            return count
        return k_most(K) - k_most(K - 1)
# @lc code=end

