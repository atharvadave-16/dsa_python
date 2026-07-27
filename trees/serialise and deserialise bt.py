from typing import TreeNode
class Codec:

    def serialize(self, root):
        res =[]
        def dfs(node):
            if not node:
                res.append("")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)        
        

    def deserialize(self, data):
        v = data.split(",")
        self.i = 0
        def dfs():
            if v[self.i] == "":
                self.i = self.i + 1
                return
            node = TreeNode(int(v[self.i]))
            self.i = self.i + 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs() 


# Pattern: Preorder DFS serialization
# Approach: serialize → preorder traversal, "" for nulls, join with ","
#           deserialize → split by ",", rebuild using same preorder order
# Key trick: self.i tracks current position across recursive calls
# TC: O(n) | SC: O(n)    