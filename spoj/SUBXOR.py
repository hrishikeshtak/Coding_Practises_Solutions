#!/usr/bin/python3

"""
Given an array of positive integers you have to print the number of
subarrays whose XOR is less than K
"""
# Optimize (Meet in the middle) Approach


def subxor(arr, N, K):
    count = 0
    first_half_xor = []
    second_half_xor = []
    first_half_xor.append(0)

    for i in range(0, N//2 + 1):
        xor = 0
        for j in range(i, N//2 + 1):
            # print(arr[j])
            xor = xor ^ arr[j]
            # print(arr[i:j+1])
            # print("xor: ", xor)

            # do not conside last element in first half
            if xor < K and j != N//2:
                count += 1
        first_half_xor.append(xor)
    # print("first_half_xor: ", first_half_xor)

    # count xor of half subarray less than K
    for i in range(1, len(first_half_xor)):
        if first_half_xor[i] < K:
            count += 1

    # print("count: ", count)
    # Take other half array
    for i in range(N//2 + 1, N):
        xor = 0
        for j in range(i, N):
            # print(arr[j])
            xor = xor ^ arr[j]
            # check only those element starting from first element
            # of second half array
            if i == (N//2 + 1):
                second_half_xor.append(xor)
            elif xor < K:
                count += 1
            # print(arr[i:j+1])
            # print("xor: ", xor)

    # print("second_half_xor: ", second_half_xor)
    for i in range(0, len(first_half_xor)):
        for j in range(0, (len(second_half_xor))):
            if second_half_xor[j] < K or (first_half_xor[i] ^ second_half_xor[j]) < K:
                # print(i, j)
                count += 1

    return count


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(subxor(arr, N, K))
