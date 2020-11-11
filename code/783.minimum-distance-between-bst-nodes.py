#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        stack = []
        ans, pre = float("inf"), float("-inf")
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ans = min(ans, root.val - pre)
                pre = root.val
                root = root.right
        
        return ans
# @lc code=end

