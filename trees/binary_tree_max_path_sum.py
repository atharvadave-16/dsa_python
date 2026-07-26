from typing import Optional
from typing import TreeNode
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       re = [root.val]
       def df(node):
            if not node:
                return 0
            l=df(node.left)
            r=df(node.right)
            l = max(l,0)
            r = max(r,0)
            re[0] = max(re[0],node.val + l + r)

            return node.val + max(l,r)
       df(root)
       return re[0]



# Pattern: DFS with global max (same as diameter)
# Approach: at each node, max path = node + left + right
# Key trick: max(l, 0) ignores negative branches
# return node + max(l,r) → only one branch goes upward
# TC: O(n) | SC: O(h)    