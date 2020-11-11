#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        res = [0]
        for c in S:
            num = widths[ord(c) - 97]
            if res[-1] + num > 100:
                res.append(num)
            else:
                res[-1] += num
        return [len(res), res[-1]]
# @lc code=end

