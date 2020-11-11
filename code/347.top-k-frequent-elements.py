#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
# O(n) + O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        q = []
        for i, v in cnt.items():
            heapq.heappush(q, (v, i))
            if len(q) > k:
                heapq.heappop(q)
        return [n for _, n  in q]
# @lc code=end

