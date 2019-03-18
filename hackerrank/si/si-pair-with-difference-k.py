#!/usr/bin/python3


def partition(arr, lo, hi):
    # last element as pivot
    i = lo - 1
    pivot = arr[hi-1]

    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
    return i + 1


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        # print(arr, p, arr[p])
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


# sort + 2 pointer technique
def pair_with_diff_k(arr, N, K):
    # print(arr)
    quick_sort(arr, 0, N)
    # print(arr)

    i = 0
    j = 0

    while j < N:
        if arr[j] - arr[i] == K:
            return "True"
        elif arr[j] - arr[i] < K:
            j += 1
        else:
            i += 1
    return "False"


for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    status = pair_with_diff_k(arr, N, K)
    print(status.lower())
