#!/usr/bin/python3

# Least common ancestor of Binary tree


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def root_to_node_path(root, A, path):
    if root is None:
        return False

    path.append(root.val)
    if root.val == A:
        return True

    if (root.left and root_to_node_path(root.left, A, path)) or \
       (root.right and root_to_node_path(root.right, A, path)):
        return True

    path.pop()
    return False


def least_common_ancestor(root, A, B):
    path1 = []
    root_to_node_path(root, A, path1)
    print(path1)
    if not path1:
        return -1

    path2 = []
    root_to_node_path(root, B, path2)
    print(path2)

    if not path2:
        return -1

    prev = -1
    for i, j in zip(path1, path2):
        if i != j:
            break
        prev = i

    return prev


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(least_common_ancestor(root, 9, 1))
