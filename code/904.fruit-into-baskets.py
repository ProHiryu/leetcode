#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, r = 0, 0
        res = 1
        types = collections.defaultdict(int)
        while r < len(tree):
            types[tree[r]] += 1
            if len(types) == 2 or len(types) == 1:
                res = max(res, r - l + 1)
            while len(types) > 2:
                types[tree[l]] -= 1
                if not types[tree[l]]:
                    del types[tree[l]]
                l += 1
            r += 1
        return res
# @lc code=end

