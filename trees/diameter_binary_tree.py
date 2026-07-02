from typing import Optional
from typing import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def df(root):
            if not root:
                return 0
            left = df(root.left)
            right = df(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        df(root)
        return self.res