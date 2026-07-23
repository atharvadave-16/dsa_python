from typing import Optional
from typing import TreeNode
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a =[]
        def df(node):
            if not node :
                return
            a.append(node.val)  
            df(node.left)
            df(node.right)
        df(root)
        b = sorted(a)
        return b[k-1]