#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]
# @lc code=end

