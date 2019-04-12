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
    # @return a list of list of integers
    def zigzagLevelOrder(self, root):
        # two stacks
        # variable to keep track of the current level order
        # (whether it is left to right or right to left)
        s1 = []
        s2 = []
        zigzag = True

        s1.append(root)
        ans = []
        res = []

        while s1:
            cur = s1.pop()
            res.append(cur.val)
            # print(cur.val, end=" ")

            if zigzag:
                if cur.left:
                    s2.append(cur.left)
                if cur.right:
                    s2.append(cur.right)
            else:
                if cur.right:
                    s2.append(cur.right)
                if cur.left:
                    s2.append(cur.left)

            # change flag when s1 done
            if len(s1) == 0:
                ans.append(res)
                res = []
                zigzag = not zigzag
                s1, s2 = s2, s1

        # print()
        return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        root = TreeNode(arr[0])
        for i in range(1, N):
            root = insertBST(root, arr[i])
        print(Solution().zigzagLevelOrder(root))
