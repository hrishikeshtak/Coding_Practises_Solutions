#!/usr/bin/python3
SIZE = 10000


class Deque:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.arr = [-1] * SIZE

    def isFull(self):
        return (self.front == 0 and self.rear == SIZE - 1) or \
            self.front == self.rear + 1

    def isEmpty(self):
        return self.front == -1 or self.rear == -1

    def insertFront(self, key):
        if self.isFull():
            # print("Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0

        elif self.front == 0:
            self.front = SIZE - 1

        else:
            self.front -= 1

        self.arr[self.front] = key

    def insertRear(self, key):
        if self.isFull():
            # print("Overflow")
            return

        if self.front == -1:
            self.front = 0
            self.rear = 0

        elif self.rear == SIZE - 1:
            self.rear = 0

        else:
            self.rear += 1

        self.arr[self.rear] = key

    def deleteFront(self):
        if self.isEmpty():
            # print("Queue Underflow")
            return

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == SIZE - 1:
            self.front = 0
        else:
            self.front += 1

    def deleteRear(self):
        if self.isEmpty():
            # print("Queue Underflow")
            return

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
            self.rear = SIZE - 1
        else:
            self.rear -= 1

    def getFront(self):
        if self.isEmpty():
            print("Empty")
            return

        print(self.arr[self.front])

    def getRear(self):
        if self.isEmpty():
            print("Empty")
            return

        print(self.arr[self.rear])


def implement_dequq(operation):
    deque = Deque()
    # import pdb; pdb.set_trace()

    for op in operation:
        if op[0].lower() == "push_front":
            x = int(op[1])
            # print(x)
            deque.insertFront(x)
        elif op[0].lower() == "push_back":
            x = int(op[1])
            deque.insertRear(x)
        elif op[0].lower() == "pop_front":
            deque.getFront()
            deque.deleteFront()
        else:
            deque.getRear()
            deque.deleteRear()


if __name__ == '__main__':
    operation = []
    for _ in range(int(input())):
        operation.append(input().split(" ", 1))
    implement_dequq(operation)
