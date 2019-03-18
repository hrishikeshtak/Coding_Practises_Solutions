#!/usr/bin/python3

# Quick Sort + Binary Search => O(NlogN + QlogN)


def partition(arr, lo, hi):
    pivot = arr[hi-1]
    i = lo - 1
    for j in range(lo, hi-1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
    return i+1


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        # print(arr, p)
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


def BS1(arr, K):
    # Return First index of element
    lo = 0
    hi = len(arr)-1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == K:
            ans = mid
            hi = mid - 1
        elif arr[mid] < K:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def BS2(arr, K):
    # Return Last index of element
    lo = 0
    hi = len(arr)-1
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == K:
            ans = mid
            lo = mid + 1
        elif arr[mid] < K:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def finding_frequency(arr, N, K):
    x = BS1(arr, K)
    y = BS2(arr, K)
    # print(x, y)
    if x == -1 or y == -1:
        return 0
    else:
        return (y - x) + 1


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    # print(arr)
    quick_sort(arr, 0, N)
    # print(arr)

    for Q in range(int(input())):
        K = int(input())
        print(finding_frequency(arr, N, K))
