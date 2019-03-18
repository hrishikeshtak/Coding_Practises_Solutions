#!/usr/bin/python3

# using merge sort


def mergesort(arr):
    N = len(arr)
    inv_count = 0
    if N > 1:
        mid = N // 2
        L = arr[:mid]
        R = arr[mid:]

        inv_count += mergesort(L)
        inv_count += mergesort(R)
        print("L: %s, inv_count: %s" % (L, inv_count))
        print("R: %s, inv_count: %s" % (R, inv_count))

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                inv_count += len(L) - i
            k += 1
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
    return inv_count


def getInvCount(arr):
    return mergesort(arr)


if __name__ == "__main__":
    arr = [1, 5, 2, 15, 3]  # 3
    # arr = [1, 20, 6, 4, 5]  # 5
    # arr = [1, 5, 2, 15, 3, 8, 7, -1, 12, 4]
    print(arr)
    print(getInvCount(arr))
    print(arr)
