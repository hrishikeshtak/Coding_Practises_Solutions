#!/usr/bin/python3

# Postorder Traversal using 2 stacks


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversalRecursive(self, root):
        if root is None:
            return

        self.postorderTraversalRecursive(root.left)
        self.postorderTraversalRecursive(root.right)
        print(root.val, end=" ")

    # using 2 stacks
    def postorderTraversalTwoStacks(self, root):
        if root is None:
            return

        stack1 = []
        stack2 = []
        cur = root

        stack1.append(root)

        while stack1:
            cur = stack1.pop()
            stack2.append(cur.val)

            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)

        return stack2[::-1]

    # using 1 stack
    def postorderTraversal(self, root):
        if root is None:
            return

        # top of stack
        def top(stack):
            if stack:
                return stack[-1]
            return None

        stack = []
        res = []
        cur = root
        done = False

        while not done:
            if cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur.right and cur.right == top(stack):
                    _ = stack.pop()
                    stack.append(cur)
                    cur = cur.right
                else:
                    res.append(cur.val)
                    cur = None

            if not stack:
                done = True

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

    print("PostorderTraversalRecursive: ")
    Solution().postorderTraversalRecursive(root)
    print("\nPostorderTraversalIterative: ")
    print(Solution().postorderTraversal(root))
    print("PostorderTraversalIterative Two stacks: ")
    print(Solution().postorderTraversalTwoStacks(root))
    print()
