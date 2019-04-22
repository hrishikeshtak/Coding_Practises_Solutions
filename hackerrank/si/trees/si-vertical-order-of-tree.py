#!/usr/bin/python3

# Level Order based Traversal
from collections import defaultdict


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertBST(self, root, key):
        if root is None:
            return TreeNode(key)
        if root.val < key:
            root.right = self.insertBST(root.right, key)
        else:
            root.left = self.insertBST(root.left, key)

        return root

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
        for key in sorted(horizontal_distances):
            print(*sorted(horizontal_distances[key]))


if __name__ == '__main__':
    for _ in range(int(input())):
        obj = Solution()
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = obj.insertBST(root, arr[i])
        obj.verticalOrderTraversal(root)
        print()
