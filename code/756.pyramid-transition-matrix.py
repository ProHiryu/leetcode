#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#

# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pool=defaultdict(list)
        for x in allowed: pool[x[:2]].append(x[2])

        def dfs(bottom):
            if len(bottom)==1: return True
            for b in product(*(pool[x+y] for x,y in zip(bottom[:-1],bottom[1:]))):
                if dfs(b): return True
            return False
        
        return dfs(bottom)
# @lc code=end

