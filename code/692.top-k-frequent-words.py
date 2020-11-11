#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        q = []
        for w, c in cnt.items():
            heapq.heappush(q, (-c, w))
        res = []
        for i in range(k):
            res.append(heapq.heappop(q)[1])
        return res
# @lc code=end

