from typing import Optional
from typing import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def issame(self,root,subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        if root.val != subroot.val:
            return False
        if root.val == subroot.val:
                    return self.issame(root.left,subroot.left) and self.issame(root.right,subroot.right) 

    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        if root.val != subroot.val:
           return  self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot)  
        if root.val == subroot.val:
           return self.issame(root,subroot) or self.isSubtree(root.right,subroot) or self.isSubtree(root.left,subroot)