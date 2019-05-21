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


def range_query(arr, A, B):
    # find lower idx of A
    lower_idx = lower_index(arr, A)
    # find upper idx of B
    upper_idx = upper_index(arr, B)
    # print(lower_idx, upper_idx)

    return (upper_idx - lower_idx) + 1


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))

        # sort the array
        arr.sort()
        # print(arr)

        Q = int(input())
        for _ in range(Q):
            A, B = map(int, input().split())
            print(range_query(arr, A, B))
