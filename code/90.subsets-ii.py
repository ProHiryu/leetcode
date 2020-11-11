#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                new_res_ = []
                for sub in new_res:
                    new_res_.append(sub + [nums[i]])
                new_res = new_res_
            else:
                new_res = []
                for sub in res:
                    new_res.append(sub + [nums[i]])
            res += new_res
        return res

# @lc code=end

