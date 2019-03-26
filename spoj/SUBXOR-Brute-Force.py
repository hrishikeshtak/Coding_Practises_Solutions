#!/usr/bin/python3

"""
Given an array of positive integers you have to print the number of
subarrays whose XOR is less than K
"""
# Brute Force O(N^2)


def subxor(arr, N, K):
    count = 0

    for i in range(0, N):
        xor = 0
        for j in range(i, N):
            # print(arr[j])
            xor = xor ^ arr[j]
            # print(arr[i:j+1])
            # print("xor: ", xor)
            if xor < K:
                count += 1

    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(subxor(arr, N, K))
