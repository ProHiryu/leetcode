#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        s = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route:
                s[j].add(i)
        
        state = set([S])
        res = 0
        while state:
            if T in state:
                return res
            new_state = set()
            for i in state:
                bus = s.pop(i, []) # 点睛之笔
                for b in bus:
                    new_state.update(routes[b])
            state = new_state
            res += 1
        return -1
# @lc code=end

