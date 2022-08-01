"""
297. Serialize and Deserialize Binary Tree
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        
        def dfs(root):
            if root is None:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = ",".join(res)
        # print(res)
        return res
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        # print(data)
        self.idx = 0
        
        def dfs():
            if data[self.idx] == 'N':
                self.idx += 1
                return None
            node = TreeNode(int(data[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
                

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))