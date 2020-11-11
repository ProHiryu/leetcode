#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                slow_ = 0
                while True:
                    slow_ = nums[slow_]
                    slow = nums[slow]
                    if slow == slow_:
                        return slow
# @lc code=end

