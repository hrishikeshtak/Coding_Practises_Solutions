#!/usr/bin/python3


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


def root_to_leaf_path(root, S, path):
    if root is None:
        return

    if not path:
        root_to_leaf_path(root.left, S, path)
    if not path:
        root_to_leaf_path(root.right, S, path)

    if root.val == S:
        path.append(root)
        return
    if path:
        path.append(root)


def count(root, d):
    if root is None:
        return 0

    if d == 0 or d == -1:
        return 1

    return count(root.left, d-1) + count(root.right, d-1)


def nodes_at_distance_k(root, S, K):
    if root is None or K < 0:
        return 0
    path = []
    root_to_leaf_path(root, S, path)
    # print("Path from root: %s to S: %s" % (root.val, S))
    # for i in path:
    #     print(i.val, end=" ")
    # print()
    cnt = 0
    cnt += count(path[0], K)
    # import pdb; pdb.set_trace()
    for i in range(1, len(path)):
        # print("s: %s cnt: %s" % (path[i].val, cnt))
        if path[i].left == path[i-1]:
            if path[i].right:
                cnt += count(path[i].right, K-i-1)
            elif path[i].right is None and K-i-1 == -1:
                cnt += 1
        else:
            if path[i].left:
                cnt += count(path[i].left, K-i-1)
            elif path[i].left is None and K-i-1 == -1:
                cnt += 1
    return cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        N, S, K = map(int, input().split())
        arr = list(map(int, input().split()))
        root = None
        for i in range(N):
            root = insert(root, arr[i])
        # inorder(root)
        # print()
        print(nodes_at_distance_k(root, S, K))
