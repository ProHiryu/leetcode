#
# @lc app=leetcode id=749 lang=python3
#
# [749] Contain Virus
#

# @lc code=start
class Solution:
    """
    思路：BFS
        1. 获取感染区、扩散区和墙数：获取感染区中所有点、及每个区域的扩散点、墙数
        2. 建墙：选取扩散点数最多的区域，统计墙数，建墙后墙内节点设置为安全区
        3. 扩散：其他区域的扩散点设为感染区
        4. 重复以上过程，直至没有感染区
    """
    def containVirus(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        
        def adj(i,j):
            for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= ii < m and 0 <= jj< n:
                    yield ii,jj
        
        def get_virus_areas(grid):
            areas = []
            dangers = []
            walls = []
            color = [[0] * n for i in range(m)]
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and color[i][j] == 0:
                        area = [(i,j)]
                        danger = set()
                        wall = 0
                        Q = [(i,j)]
                        color[i][j] = 1
                        while Q:
                            s,t = Q.pop(0)
                            for ii,jj in adj(s,t):
                                if grid[ii][jj] == 1 and color[ii][jj] == 0:
                                    color[ii][jj] = 1
                                    Q.append((ii,jj))
                                    area.append((ii,jj))
                                if grid[ii][jj] == 0:
                                    wall += 1
                                    danger.add((ii,jj))
                        areas.append(area)
                        dangers.append(danger)
                        walls.append(wall)
            return areas,dangers,walls
        
        def spread(dangers):
            for danger in dangers:
                for i,j in danger:
                    grid[i][j] = 1
        
        wall_count = 0
        areas,dangers,walls = get_virus_areas(grid)
        while areas:
            # 如果全是感染区，返回
            n_area = len(areas)
            if sum(len(area) for area in areas) == m * n:
                return wall_count
            
            # 获取危险点最多的区域
            dangerest_i = 0
            for i in range(n_area):
                if len(dangers[i]) > len(dangers[dangerest_i]):
                    dangerest_i = i
            
            # 建墙，统计墙数，将对应感染区变为安全区
            wall_count += walls[dangerest_i]
            for i,j in areas[dangerest_i]:
                grid[i][j] = -1
            
            # 其他感染区扩散
            spread(dangers[:dangerest_i] + dangers[dangerest_i+1:])
            
            # 重新获取感染区
            areas,dangers,walls = get_virus_areas(grid)
        
        return wall_count
# @lc code=end

