#!/usr/bin/python3

"""
You are given 4 arrays - A, B, C, D of integers. You have to
find the number of quadruples (i,j,k,l) such that
A[i]^B[j]^C[k]^D[l] = 0.
"""

# Using Hashing + Sort + Binary Search


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
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


def BS1(arr, X):
    # Find 1st occurence of X in arr
    lo = 0
    hi = len(arr) - 1
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == X:
            ans = mid
            hi = mid - 1
        elif arr[mid] < X:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def BS2(arr, X):
    # Find last occurence of X in arr
    lo = 0
    hi = len(arr) - 1
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == X:
            ans = mid
            lo = mid + 1
        elif arr[mid] < X:
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def quadruples(A, B, C, D, X):
    hashset_1 = list()
    hashset_2 = list()

    # store xor from pairs
    for i in range(len(A)):
        for j in range(len(B)):
            hashset_1.append(A[i] ^ B[j])
            hashset_2.append(X ^ C[i] ^ D[j])
    # print(hashset_1)
    # sort hashset_1
    quick_sort(hashset_1, 0, len(hashset_1))
    # print(hashset_1)
    # print(hashset_2)
    count = 0
    # loop thr hashset_2 and count occurence in hashset_1 using
    # Binary search
    for i in range(len(hashset_2)):
        p1 = BS1(hashset_1, hashset_2[i])
        p2 = BS2(hashset_1, hashset_2[i])
        # print(p1, hashset_2[i])
        # print(p2, hashset_2[i])
        if p1 and p2:
            count += (p2 - p1 + 1)
    return count


if __name__ == '__main__':
    X = 0
    for _ in range(int(input())):
        N = int(input())
        arr = []
        for _ in range(4):
            A = list(map(int, input().split()))
            arr.append(A)
        print(quadruples(arr[0], arr[1], arr[2], arr[3], X))
