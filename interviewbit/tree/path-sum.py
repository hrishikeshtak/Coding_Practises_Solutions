#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insertBST(root, key):
    if root is None:
        return TreeNode(key)
    if root.val < key:
        root.right = insertBST(root.right, key)
    else:
        root.left = insertBST(root.left, key)

    return root

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, root, K):
        if root is None:
            return 0

        path = []
        return self.path(root, path, K)

    def path(self, root, path, K):
        if root is None:
            return 0

        path.append(root.val)

        if root.left is None and root.right is None:
            path_sum = sum(path)
            # print(path, sum(path))
            if path_sum == K:
                return 1
        else:
            if self.path(root.left, path, K) or self.path(
                    root.right, path, K):
                return 1

        path.pop()
        return 0


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        print(Solution().hasPathSum(root, 6))
