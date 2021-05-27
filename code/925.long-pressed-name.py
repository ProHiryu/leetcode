#
# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m = len(name)
        n = len(typed)
        
        i, j = 0, 0
        while j < n:
            if (i < m) and (name[i] == typed[j]):
                i += 1
                j += 1
            else:
                if (j > 0) and (typed[j] == typed[j - 1]):
                    j += 1
                else:
                    return False
        return i == m
        
