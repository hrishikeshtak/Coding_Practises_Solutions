#!/usr/bin/python3

# Top View of Tree

from collections import defaultdict


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def top_view_traversal(self, root):
        # Level Order based traversal
        if root is None:
            return []

        q = []
        level = 0

        q.append((root, level))
        q.append(None)

        HD = defaultdict(list)

        while len(q) > 1:
            # print(q, cnt)
            cur = q.pop(0)

            if cur:
                cur, level = cur[0], cur[1]
                HD[level].append(cur.val)
                if cur.left:
                    q.append((cur.left, level - 1))
                if cur.right:
                    q.append((cur.right, level + 1))
            elif cur is None:
                q.append(None)

        print(HD)
        print("Top View")
        for i in sorted(HD):
            print(HD[i][0], end=" ")
        print()


if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(5)
    root.left = TreeNode(6)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(-1)
    root.left.left.right = TreeNode(7)
    root.left.left.right.left = TreeNode(3)
    root.left.left.right.right = TreeNode(2)
    root.left.left.right.left.left = TreeNode(2)
    root.left.left.right.left.left.left = TreeNode(-1)

    root.right = TreeNode(12)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(-9)
    root.right.right.left = TreeNode(4)
    root.right.right.left.right = TreeNode(12)
    root.right.right.left.right.right = TreeNode(13)
    root.right.right.left.right.right.right = TreeNode(15)

    obj.top_view_traversal(root)
