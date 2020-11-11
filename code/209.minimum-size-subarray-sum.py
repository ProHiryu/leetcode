#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = float("inf")
        count = 0
        l = 0
        for r, n in enumerate(nums):
            count += n
            while count >= s:
                res = min(res, r - l + 1)
                count -= nums[l]
                l += 1
        return res if res != float("inf") else 0
                
# @lc code=end

