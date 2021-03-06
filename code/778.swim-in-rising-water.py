#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    '''
    思路：
        1. 记录所有到达过的节点
        2. 使用heap保存接下来可以遍历的节点
        3. 每次都先走time消耗最小的节点，使用heappop即可
    '''
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return False
        i, j, N = 0, 0, len(grid)
        hq = [(grid[0][0], (i, j))]
        visited = set()
        visited.add((i, j))
        while True:
            time, (i, j) = heapq.heappop(hq)
            if i == N-1 and j == N-1:
                return time
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if x >= 0 and x < N and y >= 0 and y < N:
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    heapq.heappush(hq, (max(time, grid[x][y]), (x, y)))


# @lc code=end

