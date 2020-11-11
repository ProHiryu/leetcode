#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 使用index来表示不同的island
        2. 更改grid当中表示陆地的值为对应的index
        3. 先将所有的island面积计算出来，同时保存在对应index的面积中
        4. 遍历0的值，计算能够连接起来的最大值即可
    '''
    def largestIsland(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            area = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    area += dfs(i, j, index)
            return area + 1

        # DFS every island and give it an index of island
        index = 2
        area = {}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    area[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(area.values() or [0])
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y) if grid[i][j] > 1)
                    res = max(res, sum(area[index] for index in possible) + 1)
        return res
# @lc code=end

