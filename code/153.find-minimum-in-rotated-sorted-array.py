#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        res = float("inf")
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] > nums[-1]:
                l = m + 1
            else:
                r = m
        return nums[l]
# @lc code=end

