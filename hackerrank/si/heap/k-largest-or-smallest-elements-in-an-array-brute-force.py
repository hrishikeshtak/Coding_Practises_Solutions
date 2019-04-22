#!/usr/bin/python3

# using sorting


# # last element as a Pivot
# def partition(arr, lo, hi):
#     i = lo - 1
#     pivot = arr[hi-1]

#     for j in range(lo, hi):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
#     return i + 1


# first element as a Pivot
def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo
    j = hi-1
    while i < j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[lo] = arr[lo], arr[j]
    return j


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        # print("pivot: ", arr[p])
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


def kSmallest(arr, k):
    N = len(arr)
    # print("Before Sort: ", arr)
    quick_sort(arr, 0, N)
    # print("After Sort: ", arr)

    print("K: {} Smallest element: ".format(k))
    for i in range(0, k):
        print(arr[i], end=" ")
    print()


def kLargest(arr, k):
    N = len(arr)
    # print("Before Sort: ", arr)
    quick_sort(arr, 0, N)
    # print("After Sort: ", arr)

    print("K: {} Largest element: ".format(k))
    for i in range(N-1, N-k-1, -1):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 4
    print("arr: ", arr)
    kSmallest(arr, k)
    kLargest(arr, k)
