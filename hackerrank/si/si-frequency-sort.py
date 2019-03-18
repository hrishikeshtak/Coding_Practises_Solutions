#!/usr/bin/python3


def merge_sort(arr):
    """Updated merge sort to sort on key."""
    N = len(arr)
    if N > 1:
        mid = N // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        # print("L: ", L)
        # print("R: ", R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
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


def frequency_sort(arr):
    arr.sort()
    # frequency_arr contains tuple of (frequency, element)
    frequency_arr = []
    count = 1
    for i in range(0, len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1
        else:
            frequency_arr.append((count, arr[i]))
            count = 1
    # last element
    frequency_arr.append((count, arr[i+1]))
    # print(frequency_arr)
    # sort frequency_arr based on frequency
    merge_sort(frequency_arr)
    # print(frequency_arr)
    for i in frequency_arr:
        for j in range(i[0]):
            print(i[1], end=" ")
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        frequency_sort(arr)
