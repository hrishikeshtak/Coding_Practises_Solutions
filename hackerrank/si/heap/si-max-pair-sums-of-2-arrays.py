#!/usr/bin/python3


def insertMaxHeap(arr, val):
    arr.append(val)
    idx = len(arr) - 1

    while idx > 0 and arr[idx][0] > arr[(idx-1)//2][0]:
        arr[idx], arr[(idx-1)//2] = arr[(idx-1)//2], arr[idx]
        idx = (idx-1) // 2


def leftChildren(arr, idx, N):
    left = 2*idx + 1
    if left >= N:
        return -1
    return left


def rightChildren(arr, idx, N):
    right = 2*idx + 2
    if right >= N:
        return -1
    return right


def heapify(arr, idx, N):
    largest = idx
    left = leftChildren(arr, idx, N)
    right = rightChildren(arr, idx, N)

    # print(arr)
    # print("left: %s, right: %s" % (left, right))
    # print(arr[left][0], arr[largest][0])
    if left != -1 and arr[left][0] > arr[largest][0]:
        largest = left

    if right != -1 and arr[right][0] > arr[largest][0]:
        largest = right

    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        heapify(arr, largest, N)


def delMax(arr):
    temp = arr[0]
    N = len(arr)

    if N == 1:
        temp = arr.pop()
        return temp

    arr[0] = arr.pop()
    heapify(arr, 0, len(arr))
    return temp


def max_pairs_sum(A, B, N, K):
    A.sort()
    B.sort()

    # to store sum
    max_heap = []
    # to check indices are already present or not
    indices = set()

    # insert max sum along with indices
    temp = ((A[N-1] + B[N-1]), (N-1, N-1))
    insertMaxHeap(max_heap, temp)
    indices.add((N-1, N-1))
    # import pdb; pdb.set_trace()

    for i in range(0, K):
        # print("max_heap: ", max_heap)
        # print("indices: ", indices)

        temp = delMax(max_heap)
        print(temp[0], end=" ")

        # take indices of max sum
        x, y = temp[1]
        max_sum = A[x-1] + B[y]
        index = (x-1, y)

        if index[0] >= 0 and index[1] >= 0 and index not in indices:
            insertMaxHeap(max_heap, (max_sum, index))
            indices.add(index)

        max_sum = A[x] + B[y-1]
        index = (x, y-1)

        if index[0] >= 0 and index[1] >= 0 and index not in indices:
            insertMaxHeap(max_heap, (max_sum, index))
            indices.add(index)


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        max_pairs_sum(A, B, N, K)
        print()
