#!/usr/bin/python3

# using Max Heap


def LeftChildren(arr, i, N):
    left = 2 * i + 1
    if left >= N:
        return -1
    return left


def RightChildren(arr, i, N):
    right = 2 * i + 2
    if right >= N:
        return -1
    return right


def Maxheapify(arr, i, N):
    largest = i
    left = LeftChildren(arr, i, N)
    right = RightChildren(arr, i, N)

    if left != -1 and arr[left] > arr[largest]:
        largest = left

    if right != -1 and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Maxheapify(arr, largest, N)


def getMax(arr):
    return arr[0]


def kSmallest(arr, K):
    N = len(arr)
    heap = []

    # store K element in heap
    # build max heap
    for i in range(0, K):
        heap.append(arr[i])
    # print("Before heapify: ", heap)
    Maxheapify(heap, 0, K)
    # print("After heapify: ", heap)

    # iterate thr array, if arr element is less than
    # getMax of heap then replace it with getMax
    for i in range(K, N):
        if arr[i] < getMax(heap):
            heap[0] = arr[i]
            Maxheapify(heap, 0, K)

    print("K: {} Smallest element: ".format(k))
    heap.sort()
    for i in range(0, K):
        print(heap[i], end=" ")
    print()


def Minheapify(arr, i, N):
    smallest = i
    left = LeftChildren(arr, i, N)
    right = RightChildren(arr, i, N)

    if left != -1 and arr[left] < arr[smallest]:
        smallest = left

    if right != -1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        Minheapify(arr, smallest, N)


def getMin(arr):
    return arr[0]


def kLargest(arr, K):
    N = len(arr)
    heap = []

    # store K element in heap
    # build min heap
    for i in range(0, K):
        heap.append(arr[i])
    # print("Before heapify: ", heap)
    Minheapify(heap, 0, K)
    # print("After heapify: ", heap)

    # iterate thr array, if arr element is more than
    # getMin of heap then replace it with getMin
    for i in range(K, N):
        if arr[i] > getMin(heap):
            heap[0] = arr[i]
            Minheapify(heap, 0, K)

    print("K: {} Largest element: ".format(k))
    heap.sort()
    for i in range(0, K):
        print(heap[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 4
    print("arr: ", arr)
    kSmallest(arr, k)
    kLargest(arr, k)
