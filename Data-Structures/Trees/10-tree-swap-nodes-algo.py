#!/usr/bin/python3

import os
import sys

# For last 2 test cases, To avoid
# RecursionError: maximum recursion depth exceeded
sys.setrecursionlimit(15000)


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.info)


def createBinaryTree(indexes):
    # create Binary Tree from indexes list
    # initialize all nodes with values 1 to n
    nodes = list()
    for i in range(len(indexes)):
        # indices start from 0
        nodes.append(Node(i+1))

    # prepare binary tree
    for index in range(len(indexes)):
        left = indexes[index][0]
        right = indexes[index][1]
        # take values from already initialized nodes
        nodes[index].left = None if left == -1 else nodes[left-1]
        nodes[index].right = None if right == -1 else nodes[right-1]

    # return root
    return nodes[0]


def inOrder(root, result):
    # Write your code here
    if not root:
        return result
    inOrder(root.left, result)
    # print(root.info, end=' ')  # python3
    result.append(root.info)
    inOrder(root.right, result)
    return (result)


def swapEveryKLevel(root, level, k):
    if root is None or (root.left is None and
                        root.right is None):
        return

    if ((level) % k == 0):
        root.left, root.right = root.right, root.left

    swapEveryKLevel(root.left, level+1, k)
    swapEveryKLevel(root.right, level+1, k)


def swapNodes(indexes, queries):
    # create Binary Tree
    root = createBinaryTree(indexes)
    finalResult = list()
    for k in queries:
        result = list()
        # import pdb; pdb.set_trace()
        swapEveryKLevel(root, 1, k)
        # print inorder
        finalResult.append(inOrder(root, result))
    return (finalResult)


if __name__ == '__main__':
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    print(result)
