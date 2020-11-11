#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
            else:
                pos = bisect.bisect_left(lis, n)
                lis[pos] = n
        return len(lis)
# @lc code=end

