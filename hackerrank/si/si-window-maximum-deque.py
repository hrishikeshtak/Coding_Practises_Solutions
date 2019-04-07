#!/usr/bin/python3


class Deque:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.arr = [-1] * size
        self.size = size

    def isFull(self):
        return (self.front == 0 and self.rear == self.size - 1) or \
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
            self.front = self.size - 1

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

        elif self.rear == self.size - 1:
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
        elif self.front == self.size - 1:
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
            self.rear = self.size - 1
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


def window_maximum(arr, N, K):
    deque = Deque(K)
    max_sum = 0
    for i in range(0, K):
        deque.insertRear(arr[i])

    # print(deque.arr)
    max_sum += max(deque.arr)

    for i in range(1, N-K+1):
        deque.deleteFront()
        # print(deque.arr)
        deque.insertRear(arr[i+K-1])
        # print(deque.arr)
        max_sum += max(deque.arr)
    return max_sum


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(window_maximum(arr, N, K))
