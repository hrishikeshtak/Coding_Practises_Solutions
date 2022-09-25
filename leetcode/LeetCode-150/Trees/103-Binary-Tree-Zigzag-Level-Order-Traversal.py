"""
103. Binary Tree Zigzag Level Order Traversal
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        # 0: indicates Left to Right direction
        # 1: indicates Right to Left direction
        q.append(root)
        q.append(None)
        temp = []
        level = 0
        res = []
        while len(q) > 1:
            cur = q.pop(0)
            if cur:
                temp.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            else:
                if level % 2 != 0:
                    res.append(temp[::-1])
                else:
                    res.append(temp)
                temp = []
                q.append(None)
                level += 1
        if level % 2 != 0:
            res.append(temp[::-1])
        else:
            res.append(temp)
        # print(res)
        return res
            