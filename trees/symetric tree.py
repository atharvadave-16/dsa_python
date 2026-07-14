from typing import Optional
from typing import TreeNode
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isy(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isy(left.left, right.right) and isy(left.right, right.left)
        
        return isy(root.left, root.right)