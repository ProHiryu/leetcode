#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        pre = ListNode(0)
        pre.next = head
        res = pre
        while count < m:
            count += 1
            pre = head
            head = head.next
        dummy = pre
        dummy2 = head
        while count <= n:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
            count += 1
        dummy.next = pre
        dummy2.next = head
        return res.next
# @lc code=end

