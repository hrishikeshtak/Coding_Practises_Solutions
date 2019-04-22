#!/usr/bin/python3

# Least common ancestor of Binary tree


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, root, B, C):
        path1 = []
        self.root_to_node_path(root, B, path1)
        # print(path1)
        if not path1:
            return -1

        path2 = []
        self.root_to_node_path(root, C, path2)
        # print(path2)

        if not path2:
            return -1

        prev = -1
        for i, j in zip(path1, path2):
            if i != j:
                break
            prev = i

        return prev

    def root_to_node_path(self, root, A, path):
        # Top bottom apprach
        if root is None:
            return False

        path.append(root.val)
        if root.val == A:
            return True

        if self.root_to_node_path(root.left, A, path) or \
           self.root_to_node_path(root.right, A, path):
            return True

        path.pop()
        return False


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().lca(root, 9, 7))
