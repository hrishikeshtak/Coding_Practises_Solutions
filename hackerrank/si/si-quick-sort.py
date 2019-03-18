#!/usr/bin/python3


# last element as pivot
def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        # print(arr, p)
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
    return i+1


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr))
    print(arr)
# EOF
