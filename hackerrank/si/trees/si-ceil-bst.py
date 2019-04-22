#!/usr/bin/python3

# ceil value of given KEY in BST


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
    def ceil(self, root, K, ans):
        if root is None:
            return ans

        if root.val >= K:
            ans = root.val
            return self.ceil(root.left, K, ans)
        else:
            return self.ceil(root.right, K, ans)


if __name__ == '__main__':
    for _ in range(int(input())):
        obj = Solution()
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = obj.insertBST(root, arr[i])
        ans = -1
        ans = obj.ceil(root, 17, ans)
        print(ans)
