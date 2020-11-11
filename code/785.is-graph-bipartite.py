#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution:
    '''
    描边，使用字典记录所有index的情况，dfs当中处理
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]:
                        return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i):
                        return False
            return True
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not dfs(i):
                    return False
        return True
# @lc code=end

