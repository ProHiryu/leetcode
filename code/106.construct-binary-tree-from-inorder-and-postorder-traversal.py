#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build_tree(i, post):
            if not post:
                return None
            node = TreeNode(post[-1])
            index = i.index(post[-1])
            node.left = build_tree(i[:index], post[:index])
            node.right = build_tree(i[index + 1:], post[index:-1])
            return node
        return build_tree(inorder, postorder)
# @lc code=end

