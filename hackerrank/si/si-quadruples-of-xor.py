#!/usr/bin/python3

"""
You are given 4 arrays - A, B, C, D of integers. You have to
find the number of quadruples (i,j,k,l) such that
A[i]^B[j]^C[k]^D[l] = 0.
"""
# using Hashing
# Time Complexity = O(N^2 + N^2)
from collections import defaultdict


def quadruples(A, B, C, D, X):
    hashset_1 = defaultdict(lambda: 0)

    # store count of A[i] ^ B[j] in dict
    for i in range(len(A)):
        for j in range(len(B)):
            hashset_1[(A[i] ^ B[j])] += 1

    # print(hashset_1)
    count = 0
    for i in range(len(C)):
        for j in range(len(D)):
            if (X ^ C[i] ^ D[j]) in hashset_1:
                count += hashset_1[(X ^ C[i] ^ D[j])]

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
