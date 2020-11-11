#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new_res = []
            for sub in res:
                new_res.append(sub + [n])
            res += new_res
        return res
# @lc code=end

