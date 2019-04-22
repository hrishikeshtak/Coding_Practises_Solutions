#!/usr/bin/python3


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

    # find smallest number from left and right children
    smallest = i
    if left != -1 and arr[left] < arr[smallest]:
        smallest = left
    if right != -1 and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest, N)


def getMin(arr):
    return arr[0]


def delMin(arr, N):
    N = len(arr)
    if N == 1:
        return -1

    tmp = arr[0]
    # print("Before delMin: ", arr)
    arr[0] = arr.pop()
    N = len(arr)
    heapify(arr, 0, N)
    # print("After delMin: ", arr)
    return tmp


def insert(arr, x):
    # print("Before insert: ", arr)
    arr.append(x)
    N = len(arr)
    idx = N - 1

    while idx > 0 and arr[idx] < arr[(idx-1)//2]:
        arr[idx], arr[(idx-1)//2] = arr[(idx-1)//2], arr[idx]
        idx = (idx - 1) // 2
    # print("After insert: ", arr)


def sweetness(arr, N, K):
    # build Min Heap
    # print("Before Minheap: ", arr)
    for i in range(N-1, -1, -1):
        heapify(arr, i, N)
    # print("After Minheap: ", arr)

    # first element
    cnt = 0
    # sweetness  Least sweet cookie   2nd least sweet cookie).
    if getMin(arr) >= K:
        return cnt

    while getMin(arr) < K:
        ans = delMin(arr, N)
        # delete Min from heap
        a = delMin(arr, N)
        if ans == -1 or a == -1:
            return -1
        ans = (1 * ans) + (2 * a)
        # insert ans and apply min heap property
        insert(arr, ans)
        cnt += 1

    return cnt


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sweetness(arr, N, K))
