"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”

notes and review:
- BST properties save you from implementing Euler' tour algorithm.
- Euler' tour algorithm is a general algorithm for Binary Tree. (solve the related problems)
-
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        larger = max(p.val, q.val)
        smaller = min(p.val, q.val)
        while root:
            if root.val > larger:
                root = root.left
            elif root.val < smaller:
                root = root.right
            else:
                return root


