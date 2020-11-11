#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leafs(root):
            if not root: return
            if not root.left and not root.right:
                yield root.val
            yield from get_leafs(root.left)
            yield from get_leafs(root.right)
        return all( a == b for a, b in zip_longest(get_leafs(root1), get_leafs(root2)))
# @lc code=end

