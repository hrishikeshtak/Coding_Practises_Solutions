#!/usr/bin/python3

# Level Order based Traversal
from collections import defaultdict


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, root):
        # Level Order based traversal
        # store horizontal distance of each node from root node
        if root is None:
            return []

        horizontal_distances = defaultdict(list)

        # to store level order traversal of tree
        q = []
        q.append(root)

        # HD of root is 0
        horizontal_distances[0].append(root.val)

        # HD of cur root
        hd = {}
        hd[root] = 0

        while q:
            cur = q.pop(0)

            if cur.left:
                q.append(cur.left)
                hd[cur.left] = hd[cur] - 1
                horizontal_distances[hd[cur.left]].append(cur.left.val)

            if cur.right:
                q.append(cur.right)
                hd[cur.right] = hd[cur] + 1
                horizontal_distances[hd[cur.right]].append(cur.right.val)

        # print(horizontal_distances)
        res = []
        for key in sorted(horizontal_distances):
            res.append(horizontal_distances[key])
            # print(horizontal_distances[key])
        return res


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(10)
    root.left.right.right.left = TreeNode(30)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(8)

    print(Solution().verticalOrderTraversal(root))
