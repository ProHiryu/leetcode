#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if not any([digit == '0' or num % int(digit) != 0 for digit in str(num)])]
# @lc code=end

