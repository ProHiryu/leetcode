#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = ListNode(0)
        node = res
        q = []
        for i, n in enumerate(lists):
            if n:
                q.append((n.val, i, n))
        heapq.heapify(q)
        while len(q) > 0:
            v, i, n = heapq.heappop(q)
            node.next = n
            node = node.next
            n = n.next
            if n:
                heapq.heappush(q, (n.val, i, n))
        return res.next
# @lc code=end

