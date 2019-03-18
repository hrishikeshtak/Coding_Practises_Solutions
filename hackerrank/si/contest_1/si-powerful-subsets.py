#!/usr/bin/python3

# Brute Force
from functools import reduce

M = int(1e9 + 7)


def check_bit(i, j):
    if (i >> j) & 1:
        return True
    else:
        return False


def count_set_bits(i):
    count = 0
    while i:
        i = i & (i-1)
        count += 1
    return count


def compute_a_power_b(a, b):
    x = a
    ans = 1
    while b != 0:
        if b & 1:
            ans = ((ans % M) * (x % M)) % M
        x = ((x % M) * (x % M)) % M
        b >>= 1
    return ans


def is_powerful_subsets(subsets):
    # count set bits in subsets
    # take AND of all elements of subsets, and then count set bits
    # if set bit count is 1 then powerful subset
    anding = reduce(lambda x, y: x & y, subsets)
    if count_set_bits(anding) == 1 and anding != 1:
        return("YES")
    return("NO")


def powerful_subsets(arr):
    N = len(arr)
    for i in range(1, compute_a_power_b(2, N)):
        subsets = []
        for j in range(N):
            if check_bit(i, j):
                subsets.append(arr[j])
        # print(subsets)
        status = is_powerful_subsets(subsets)
        if status == "YES":
            return "YES"
    return "NO"


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(powerful_subsets(arr))
