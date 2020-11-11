#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#

# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            if abs(target[0] - x) + abs(target[1] - y) <= dist:
                return False
        return True
# @lc code=end

