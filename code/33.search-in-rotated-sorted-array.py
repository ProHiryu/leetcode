#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[-1]:
                if nums[mid] < target and nums[-1] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target and nums[0] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
        return l if nums[l] == target else -1
# @lc code=end

