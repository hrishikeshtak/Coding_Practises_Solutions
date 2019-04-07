#!/usr/bin/python3


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def createSLL(head, d):
    node = createNode(d)
    # add node at front
    node.next = head
    head = node
    return head


def displaySLL(root):
    cur = root
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def stack(head, operation):
    if operation[0].lower() == "push":
        x = int(operation[1])
        # print(x)
        head = createSLL(head, x)
        # top += 1
    elif operation[0].lower() == "pop":
        top = head
        if top is None:
            print("Empty")
        else:
            print(top.data)
            top = top.next
            head = top
    return head


if __name__ == '__main__':
    head = None
    for _ in range(int(input())):
        operation = input().split(" ", 1)
        head = stack(head, operation)
        # displaySLL(head)
