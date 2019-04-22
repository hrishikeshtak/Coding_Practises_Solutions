#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def pathSum(self, root, K):
        all_paths = []

        if not root:
            return all_paths

        def pathSumRec(root, path):
            if root is None:
                return 0

            path.append(root.val)

            if root.left is None and root.right is None:
                path_sum = sum(path)
                # print(path, sum(path))
                if path_sum == K:
                    all_paths.append(list(path))
                    # print(path)

            if root.left:
                pathSumRec(root.left, path)
            if root.right:
                pathSumRec(root.right, path)
            path.pop()

        pathSumRec(root, [])

        # print(all_paths)
        return all_paths


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print(Solution().pathSum(root, 22))
