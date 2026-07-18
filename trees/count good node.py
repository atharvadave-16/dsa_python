class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def df(node, maxSoFar):
            if not node:
                return 0
            count = 1 if node.val >= maxSoFar else 0
            maxSoFar = max(maxSoFar, node.val)
            return count + df(node.left, maxSoFar) + df(node.right, maxSoFar)
        
        return df(root, float('-inf'))