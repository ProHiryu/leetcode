#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        hq, t, adj = [(0, K)], {}, collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        while hq:
            time, node = heapq.heappop(hq)
            if node not in t:
                t[node] = time
                for v, w in adj[node]:
                    heapq.heappush(hq, (w + time, v))
        return max(t.values()) if len(t) == N else -1
# @lc code=end

