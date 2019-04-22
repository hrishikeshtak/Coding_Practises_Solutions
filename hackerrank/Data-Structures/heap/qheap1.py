#!/usr/bin/python3


def LeftChildren(heap, i, N):
    left = 2 * i + 1
    if left >= N:
        return -1
    return left


def RightChildren(heap, i, N):
    right = 2 * i + 2
    if right >= N:
        return -1
    return right


def heapify(heap, i, N):
    smallest = i
    left = LeftChildren(heap, i, N)
    right = RightChildren(heap, i, N)

    if left != -1 and heap[left] < heap[smallest]:
        smallest = left
    if right != -1 and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, smallest, N)


def insert(heap, x):
    # print("Before insert: ", heap)
    heap.append(x)
    N = len(heap)
    # heapify(heap, 0, N)
    idx = N - 1

    while idx > 0 and heap[idx] < heap[(idx-1) // 2]:
        heap[idx], heap[(idx-1)//2] = heap[(idx-1)//2], heap[idx]
        idx = (idx - 1) // 2
    # print("After insert: ", heap)


def delete(heap, x):
    # print("Before delete: ", heap)
    N = len(heap)
    for i in range(0, N):
        if heap[i] == x:
            heap[i], heap[N-1] = heap[N-1], heap[i]
            break
    _ = heap.pop()
    N = len(heap)
    heapify(heap, i, N)
    # print("After delete: ", heap)


def getMin(heap):
    return heap[0]


if __name__ == '__main__':
    heap = []
    for _ in range(int(input())):
        query = input().split(" ", 1)
        if query[0] == '1':
            insert(heap, int(query[1]))
        elif query[0] == '2':
            delete(heap, int(query[1]))
        else:
            print(getMin(heap))
