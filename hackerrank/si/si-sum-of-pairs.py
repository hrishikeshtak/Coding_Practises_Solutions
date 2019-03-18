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
            if L[i] < R[j]:
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


def sum_of_pairs(arr, N, K):
    # print(arr)
    merge_sort(arr)
    # print(arr)

    i = 0
    j = N-1
    while i < j:
        if arr[i] + arr[j] == K:
            return True
        elif arr[i] + arr[j] > K:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(sum_of_pairs(arr, N, K))
