"""236. Lowest Common Ancestor of a Binary Tree"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # using Path logic
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = []  # to store path from root to p
        path2 = []  # to store path from root to q
        self.findPath(root, path1, p)
        self.findPath(root, path2, q)
        # print(f"path1: {path1}")
        # print(f"path2: {path2}")

        # Compare the paths to get the first different value
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] == path2[i]:
                i += 1
            else:
                break
        return path1[i-1]

    def findPath(self, root, path, x):
        if not root:
            return False

        path.append(root.val)
        if root.val == x:
            return True
        if ((root.left and self.findPath(root.left, path, x)) or (root.right and self.findPath(root.right, path, x))):
            return True
        path.pop()
        return False

    # Time: O(n)
    # Space: O(1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root
        return left_lca if left_lca is not None else right_lca


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.left = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = 5
q = 0
print(f"LCA of p: {p} and q: {q} is = {Solution().lowestCommonAncestor(root, p, q)}")
