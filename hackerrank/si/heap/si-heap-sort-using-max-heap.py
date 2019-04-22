#!/usr/bin/python3

# Heap sort using Max Heap
# 0 based index


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


def heapify(arr, i, N):
    left = LeftChildren(arr, i, N)
    right = RightChildren(arr, i, N)
    maximum = i

    if left != -1 and arr[left] > arr[maximum]:
        maximum = left
    if right != -1 and arr[right] > arr[maximum]:
        maximum = right

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, maximum, N)


def heapSort(arr, N):

    print("Build MaxHeap")
    for i in range(N-1, -1, -1):
        heapify(arr, i, N)
    print(arr)

    print("Heap Sort")
    # first element is a largest element
    for i in range(N-1, 0, -1):
        # swap 1st and last element
        arr[0], arr[i] = arr[i], arr[0]
        # first element is a largest element
        heapify(arr, 0, i)
    print(arr)


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    heapSort(arr, len(arr))
