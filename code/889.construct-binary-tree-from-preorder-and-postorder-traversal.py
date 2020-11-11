#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def buid_tree(pre, post):
            if not pre:
                return None
            node = TreeNode(pre[0])
            if len(pre) < 2:
                return node
            index = post.index(pre[1])
            node.left = buid_tree(pre[1:2+index], post[:index+1])
            node.right = buid_tree(pre[2+index:], post[index+1:])
            return node
        return buid_tree(pre, post)
# @lc code=end

