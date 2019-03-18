#!/usr/bin/python3


# first element as pivot
def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        print(arr, p, arr[p])
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


def partition(arr, lo, hi):
    i = lo
    j = hi - 1
    pivot = arr[lo]

    while i < j:
        while arr[i] <= pivot and i < j:
            i += 1
        while arr[j] > pivot and j >= i:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[lo], arr[j] = arr[j], arr[lo]
    return j


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr))
    print(arr)
# EOF
