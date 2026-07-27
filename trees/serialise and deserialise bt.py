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