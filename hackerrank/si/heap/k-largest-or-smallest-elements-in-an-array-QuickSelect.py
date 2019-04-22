#!/usr/bin/python3

# using Quick Select


def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi]

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[hi] = arr[hi], arr[i+1]
    return i + 1


def kSmallestUtil(arr, lo, hi, K):
    if K > 0 and K <= hi - lo + 1:
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, lo, hi)
        print("pivot: ", arr[pos])

        # If position is same as k
        if (pos - lo == K - 1):
            return pos

        # if position is more, recur for left subarray
        if pos - lo > K - 1:
            return kSmallestUtil(arr, lo, pos-1, K)

        # Else recur for right subarray
        return kSmallestUtil(arr, pos+1, hi, K - (pos - lo + 1))


def kSmallest(arr, K):
    N = len(arr)
    pos = kSmallestUtil(arr, 0, N-1, K)
    for i in range(0, pos+1):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    K = 5
    print("arr: ", arr)
    kSmallest(arr, K)
