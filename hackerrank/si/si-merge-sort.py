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
                arr[k] = R[k]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
    print(arr)


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    merge_sort(arr)
