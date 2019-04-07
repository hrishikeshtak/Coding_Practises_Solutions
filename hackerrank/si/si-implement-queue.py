#!/usr/bin/python3

# Queue using SLL


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createNode(data):
    node = Node(data)
    return node


def createSLL(head, d, rare):
    rare = createNode(d)
    if head is None:
        return rare, rare

    cur = head
    while cur.next:
        cur = cur.next

    cur.next = rare
    return head, rare


def displaySLL(root):
    cur = root
    while cur:
        print(cur.data, end=" ")
        cur = cur.next
    print()


def queue(head, operation, rare):
    if operation[0].lower() == "enqueue":
        x = int(operation[1])
        # print(x)
        head, rare = createSLL(head, x, rare)
        # top += 1
    elif operation[0].lower() == "dequeue":
        if head is None:
            print("Empty")
        else:
            print(head.data)
            head = head.next
    return head


if __name__ == '__main__':
    head = None
    rare = None
    for _ in range(int(input())):
        operation = input().split(" ", 1)
        head = queue(head, operation, rare)
        # displaySLL(head)
