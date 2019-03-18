#!/usr/bin/python3

# Quick Sort + Binary Search => O(NlogN + 2logN)
# compress to A, B array


# def partition(arr, lo, hi):
#     pivot = arr[hi-1]
#     i = lo - 1
#     for j in range(lo, hi-1):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
#     return i+1


# def quick_sort(arr, lo, hi):
#     if lo < hi:
#         p = partition(arr, lo, hi)
#         # print(arr, p)
#         quick_sort(arr, lo, p)
#         quick_sort(arr, p+1, hi)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # copy remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def BS(arr, K):
    # Return index of element
    lo = 0
    hi = len(arr)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def finding_frequency(arr, query_arr):
    N = len(arr)
    # Q = query_arr[:]
    # print(query_arr)
    # # quick_sort(arr, 0, N)
    # merge_sort(query_arr)
    # print(query_arr)
    # # create B array: containing occurences of query array element
    # B = []
    # x = arr[0]
    # count = 0
    # for i in range(0, N):
    #     if arr[i] == x:
    #         count += 1
    #     else:
    #         A.append(x)
    #         B.append(count)
    #         count = 1
    #         x = arr[i]
    # # for last element
    # A.append(x)
    # B.append(count)

    for k in query_arr:
        count = 0
        for i in arr:
            if i == k:
                count += 1
        print(count)
    # # print(A)
    # # print(B)
    # index = BS(A, K)
    # # print(index)
    # if index == -1:
    #     return 0
    # else:
    #     return B[index]


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    # print(finding_frequency(arr, -1))
    query_arr = []
    for _ in range(int(input())):
        K = int(input())
        query_arr.append(K)
    finding_frequency(arr, query_arr)
