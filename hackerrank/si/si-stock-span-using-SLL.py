#!/usr/bin/python3

# Optimal: Find first max on left side


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def push(head, d):
    node = createNode(d)
    # add node at front
    node.next = head
    head = node
    return head


def pop(cur):
    cur = cur.next
    return cur


def stock_pain(arr, N):
    result = [1] * N
    head = None
    top = push(head, 0)

    i = 1
    while i < N:
        if top is None or (arr[i] < arr[top.data]):
            if top is None:
                result[i] = -1
            else:
                result[i] = top.data
            top = push(top, i)
            i += 1
        else:
            top = pop(top)

    print(result[0], end=" ")
    for i in range(1, N):
        print(i - result[i], end=" ")


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        stock_pain(arr, N)
        print()
