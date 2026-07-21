from typing import Optional
from typing import TreeNode
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result =[]
        def df(node,level):
            if not node :
                return 
            
            if level == len(result):
         
             result.append(node.val)  
            df(node.right, level + 1)
            df(node.left, level + 1)   
        df(root,0) 
        return result  