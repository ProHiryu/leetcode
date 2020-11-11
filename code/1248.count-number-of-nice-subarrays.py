#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def Most(k):
            res = 0
            l = 0
            for r in range(len(nums)):
                k -= nums[r] % 2
                while k < 0:
                    k += nums[l] % 2
                    l += 1
                res += r - l + 1
            return res
        return Most(k) - Most(k - 1)
# @lc code=end

