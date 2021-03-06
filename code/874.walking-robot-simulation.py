#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        obs = set()
        for x, y in obstacles:
            obs.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, i = 0, 0, 0
        for c in commands:
            if c == -2:
                i -= 1
            elif c == -1:
                i += 1
            else:
                i = i % 4
                dx, dy = directions[i]
                if dx:
                    for j in range(1, c + 1):
                        x += dx
                        if (x, y) in obs:
                            x -= dx
                            break
                else:
                    for j in range(1, c + 1):
                        y += dy
                        if (x, y) in obs:
                            y -= dy
                            break
                res = max(res, x * x + y * y)
        return res

# @lc code=end

