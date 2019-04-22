#!/usr/bin/python3


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
    def left_view_traversal(self, root):
        # Level Order based traversal
        if root is None:
            return []

        q = []
        q.append(root)
        q.append(None)
        cnt = 0
        # store nodes in res array
        res = []

        while len(q) > 1:
            # print(q, cnt)
            cur = q.pop(0)
            cnt += 1

            if cur:
                if cnt == 1:
                    res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            elif cur is None:
                q.append(None)
                cnt = 0

        return res


if __name__ == '__main__':
    for _ in range(int(input())):
        obj = Solution()
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = obj.insertBST(root, arr[i])
        res = obj.left_view_traversal(root)
        print(*res)
        # print()
