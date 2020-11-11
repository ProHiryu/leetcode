#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < len(nums) and nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
# @lc code=end

