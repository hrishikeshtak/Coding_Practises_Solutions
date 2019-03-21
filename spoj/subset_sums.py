#!/usr/bin/python3

M = int(1e9 + 7)

"""
Given a sequence of N (1 ≤ N ≤ 34) numbers S1, ..., SN
(-20,000,000 ≤ Si ≤ 20,000,000), determine how many subsets of S
(including the empty one) have a sum between A and B
(-500,000,000 ≤ A ≤ B ≤ 500,000,000), inclusive.
"""


def a_power_b(A, B):
    x = A
    ans = 1
    while B:
        if B & 1:
            ans = ((ans % M) * (x % M)) % M
        x = x * x
        B >>= 1
    return ans


def subset_sum(arr, N, A, B):
    M = a_power_b(2, N)
    # print(M)
    count = 0
    for i in range(0, M):
        _sum = 0
        for j in range(N):
            if (i >> j) & 1:
                _sum += arr[j]
        if _sum in range(A, B+1):
            count += 1
    return count


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    print(subset_sum(arr, N, A, B))
