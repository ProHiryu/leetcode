#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r - l) // 2
            if sum([ceil(x / mid) for x in piles]) > H:
                l = mid + 1
            else:
                r = mid
        return l
# @lc code=end

