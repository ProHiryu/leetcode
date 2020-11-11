#
# @lc app=leetcode id=807 lang=python3
#
# [807] Max Increase to Keep City Skyline
#

# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        skyline_tb = [max(line) for line in grid]
        skyline_lr = [max(line) for line in zip(*grid)]
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(skyline_tb[i], skyline_lr[j]) - grid[i][j] if grid[i][j] < min(skyline_tb[i], skyline_lr[j]) else 0
        
        return res
# @lc code=end

