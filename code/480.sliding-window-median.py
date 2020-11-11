#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
import bisect
# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = []
        res = []
        for i in range(len(nums)):
            bisect.insort(window, nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
            if len(window) == k:
                res.append((window[k//2] + window[~k//2])/2)
        return res
# @lc code=end

