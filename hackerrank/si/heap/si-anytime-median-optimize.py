#!/usr/bin/python3

# using Heap (NLogN)
# Maintain left side in max heap and
# right side in min heap
# ans is getMax from left side


def getMax(arr):
    return arr[0]


def getMin(arr):
    return arr[0]


def LeftChildren(arr, i):
    left = 2*i + 1
    if left >= len(arr):
        return -1
    return left


def RightChildren(arr, i):
    right = 2*i + 2
    if right >= len(arr):
        return -1
    return right


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def check_property(arr1, arr2):
    return (len(arr1) - len(arr2) in [0, 1])


def insertMaxHeap(max_heap, val):
    # 0 based index
    max_heap.append(val)
    idx = len(max_heap) - 1

    while idx > 0 and max_heap[(idx)] > max_heap[(idx-1)//2]:
        swap(max_heap, idx, (idx-1)//2)
        idx = (idx-1)//2


def insertMinHeap(min_heap, val):
    # 0 based index
    min_heap.append(val)
    idx = len(min_heap) - 1

    while idx > 0 and min_heap[(idx)] < min_heap[(idx-1)//2]:
        swap(min_heap, idx, (idx-1)//2)
        idx = (idx-1)//2


def delMin(min_heap):
    min_heap[0] = min_heap.pop()
    min_heapify(min_heap, 0)


def min_heapify(arr, idx):
    left = LeftChildren(arr, idx)
    right = RightChildren(arr, idx)

    smallest = idx
    if left != -1 and arr[left] < arr[smallest]:
        smallest = left

    if right != -1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != idx:
        swap(arr, idx, smallest)
        min_heapify(arr, smallest)


def delMax(max_heap):
    max_heap[0] = max_heap.pop()
    max_heapify(max_heap, 0)


def max_heapify(arr, idx):
    left = LeftChildren(arr, idx)
    right = RightChildren(arr, idx)

    largest = idx
    if left != -1 and arr[left] > arr[largest]:
        largest = left

    if right != -1 and arr[right] > arr[largest]:
        largest = right

    if largest != idx:
        swap(arr, idx, largest)
        max_heapify(arr, largest)


def anytime_median(arr, N):
    max_heap = []
    min_heap = []

    i = 0
    while i <= N:
        # print("i: ", i)
        # print("max_heap: ", max_heap)
        # print("min_heap: ", min_heap)
        if check_property(max_heap, min_heap):
            if i == N:
                break
            if max_heap and arr[i] > getMax(max_heap):
                insertMinHeap(min_heap, arr[i])
                i += 1
            else:
                insertMaxHeap(max_heap, arr[i])
                i += 1
        else:
            if (len(max_heap) - len(min_heap)) < 0:
                tmp = getMin(min_heap)
                delMin(min_heap)
                insertMaxHeap(max_heap, tmp)
            elif (len(max_heap) - len(min_heap)) > 1:
                tmp = getMax(max_heap)
                delMax(max_heap)
                insertMinHeap(min_heap, tmp)
        if check_property(max_heap, min_heap):
            print(getMax(max_heap), end=" ")
        # if i == N:
        #     break


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        anytime_median(arr, N)
        print()
