#!/usr/bin/python3

# NlogN + QlogN


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi-1]
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
    return i + 1


def finding_the_floor(arr, X):
    ans = -(1 << 31)
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= X:
            ans = arr[mid]
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    quick_sort(arr, 0, len(arr))
    # print(arr)
    for _ in range(int(input())):
        X = int(input())
        print(finding_the_floor(arr, X))
