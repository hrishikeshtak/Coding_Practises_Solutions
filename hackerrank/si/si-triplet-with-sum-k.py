#!/usr/bin/python3


def merge_sort(arr):
    N = len(arr)

    if N > 1:
        mid = N // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def triplet_with_sum_k(arr, N, K):
    # print(arr)
    merge_sort(arr)
    # print(arr)

    j = N - 1
    for i in range(0, N):
        k = i + 1
        while k < j:

    


if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(triplet_with_sum_k(arr, N, K))
