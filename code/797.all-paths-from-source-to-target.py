#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        paths = [[0]]
        while paths:
            path = paths.pop()
            for n in graph[path[-1]]:
                if n == len(graph) - 1:
                    res.append(path + [n])
                else:
                    paths.append(path + [n])
        return res
# @lc code=end

