#!/usr/bin/python3


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversalRecursive(self, root):
        if root is None:
            return

        self.inorderTraversalRecursive(root.left)
        print(root.val, end=" ")
        self.inorderTraversalRecursive(root.right)

    def inorderTraversal(self, root):
        stack = []
        res = []
        cur = root

        done = False

        while not done:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                if stack:
                    cur = stack.pop()
                    res.append(cur.val)
                    # print(cur.val, end=" ")

                    cur = cur.right
                else:
                    done = True
        # print()
        return res


if __name__ == '__main__':
    root = None
    root = TreeNode(5)
    root.left = TreeNode(10)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(-1)
    root.left.right.right = TreeNode(12)
    root.right = TreeNode(-3)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(8)

    print("InorderTraversalRecursive: ")
    Solution().inorderTraversalRecursive(root)
    print("\nInorderTraversalIterative: ")
    print(Solution().inorderTraversal(root))
    print()
