#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, a: List[int]) -> List[int]:
        i = 0 # pointer for even misplaced
        j = 1 # pointer for odd misplaced
        sz = len(a)
        
        # invariant: for every misplaced odd there is misplaced even
        # since there is just enough space for odds and evens

        while i < sz and j < sz:
            if a[i] % 2 == 0:
                i += 2
            elif a[j] % 2 == 1:
                j += 2
            else:
                # a[i] % 2 == 1 AND a[j] % 2 == 0
                a[i],a[j] = a[j],a[i]
                i += 2
                j += 2

        return a
# @lc code=end

