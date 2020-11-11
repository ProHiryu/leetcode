#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1
# @lc code=end

