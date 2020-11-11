#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = 0
        G = set(G)
        while head:
            if head.val in G:
                res += 1
                while head and head.val in G:
                    head = head.next
            else:
                head = head.next
        return res
# @lc code=end

