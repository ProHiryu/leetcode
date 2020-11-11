#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build_tree(pre, i):
            if not pre:
                return None
            node = TreeNode(pre[0])
            index = i.index(pre[0])
            node.left = build_tree(pre[1:1+index], i[:index])
            node.right = build_tree(pre[1+index:], i[index+1:])
            return node
        return build_tree(preorder, inorder)
# @lc code=end

