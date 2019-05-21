#!/usr/bin/python3

# using binary search
# find lower idx and upper idx


def lower_index(arr, K):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] >= K:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo


def upper_index(arr, K):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= K:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi


def range_query(indices, A, B):
    if A == 0:
        return indices[B][1]

    return indices[B][1] - indices[A][0] + 1


def store_indices(arr, K):
    indices = {}
    for i in range(0, K+1):
        indices[i] = (lower_index(arr, i), upper_index(arr, i))
    return indices


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))

        # sort the array
        arr.sort()
        # print(arr)
        # store lower and upper index of each number
        indices = store_indices(arr, K)

        Q = int(input())
        for _ in range(Q):
            A, B = map(int, input().split())
            print(range_query(indices, A, B))
