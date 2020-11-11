#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        while l1 or l2:
            if not l1:
                node.next = l2
                l2 = l2.next
            elif not l2:
                node.next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
            node = node.next
        return res.next
# @lc code=end

