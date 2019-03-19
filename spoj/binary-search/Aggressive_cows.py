#!/usr/bin/python3
"""
AGGRCOW - Aggressive cows
Farmer John has built a new long barn, with N (2 <= N <= 100,000)
stalls. The stalls are located along a straight line at positions
x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become
aggressive towards each other once put into a stall.
To prevent the cows from hurting each other, FJ wants to assign
the cows to the stalls, such that the minimum distance between any
two of them is as large as possible.
What is the largest minimum distance?
"""


def aggressive_cows(arr, N, C):
    # print(arr)
    merge_sort(arr)
    # print(arr)

    lo = 0
    hi = arr[N-1] - arr[0]

    ans = -1
    while lo < hi:
        mid = (lo + hi) // 2
        if valid(arr, mid, C):
            ans = max(ans, mid)
            lo = mid + 1
        else:
            hi = mid
    return ans


def valid(arr, mid, C):
    cows = 1
    min_diff = 0
    # print(arr[0], end=" ")
    for i in range(1, len(arr)):
        min_diff += arr[i] - arr[i-1]
        if min_diff >= mid:
            cows += 1
            # print(arr[i-1], end=" ")
            min_diff = 0
            if cows == C:
                return True
    return False


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


for _ in range(int(input())):
    N, C = map(int, input().split())
    arr = []
    # for _ in range(N):
    #     arr.append(int(input()))
    arr = list(map(int, input().split()))
    print(aggressive_cows(arr, N, C))
