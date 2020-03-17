#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                pre, las = s[l:r], s[l + 1:r + 1]
                return pre[::-1] == pre or las[::-1] == las
            else:
                l += 1
                r -= 1
        return True
# @lc code=end

