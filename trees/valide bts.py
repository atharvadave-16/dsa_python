from typing import Optional
from typing import TreeNode
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def df(node, minVal, maxVal):
         if not node:
           return True
         if not (minVal < node.val < maxVal):
           return False
         return df(node.left, minVal, node.val) and df(node.right, node.val, maxVal)

        return df(root, float('-inf'), float('inf'))