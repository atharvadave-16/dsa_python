from typing import Optional
from typing import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val 
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        a =  []
        def iot(node):
         if not node:
             return
         iot(node.left)
         a.append(node.val)
         iot(node.right)
        iot(root)
        return a 