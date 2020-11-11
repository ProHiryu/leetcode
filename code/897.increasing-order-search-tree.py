#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = node = TreeNode(0)
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                node.right = TreeNode(root.val)
                node = node.right
                root = root.right

        return res.right
# @lc code=end

