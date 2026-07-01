from typing import Optional


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # type: ignore
       if not root:
        return None
       root.left, root.right = root.right, root.left
       self.invertTree(root.left)
       self.invertTree(root.right)
       return root