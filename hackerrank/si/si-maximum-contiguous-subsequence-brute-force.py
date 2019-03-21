#!/usr/bin/python3

INT_MIN = -(1 << 31)
M = int(1e9 + 7)

# O(2**N)


def a_power_b(a, b):
    ans = 1
    x = a
    while b:
        if b & 1:
            ans = ((ans % M) * (x % M)) % M
        x = x * x
        b >>= 1
    return ans


def max_contiguous_subsequence(arr, N):
    ans = INT_MIN
    M = a_power_b(2, N)
    # print(M)
    for i in range(1, M):
        temp = INT_MIN
        count = 0
        for j in range(N):
            if (i >> j) & 1:
                # print(arr[j], end=" ")
                if arr[j] > temp:
                    count += 1
                temp = arr[j]
        # print()
        ans = max(ans, count)
    return ans - 1


for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    print(max_contiguous_subsequence(arr, N))
