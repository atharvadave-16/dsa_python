# Definition for a binary tree node.
from typing import Optional
from typing import TreeNode
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    
     a = []
     def dfs(node):
         if not node:
             return
         a.append(node.val)  # root first
         dfs(node.left)      # then left
         dfs(node.right)     # then right
     dfs(root)
     return a