#!/usr/bin/python3

# Optimize O(N)
from collections import defaultdict


def valid_subarrays(arr, N):
    first_indices = defaultdict(lambda: 0)
    # replace all 0 with -1
    for i in range(0, N):
        if arr[i] == 0:
            arr[i] = -1

    # print(arr)
    # Take Prefix sum
    prefix_sum = 0
    for i in range(0, N):
        arr[i] += prefix_sum
        prefix_sum = arr[i]
    # print(arr)

    # store no of occurences
    for i in range(0, N):
        first_indices[arr[i]] += 1

    # print("first_indices: ", first_indices)

    count = 0
    # if occurences of element is > 1, then no of valid_subarrays
    # = n * (n-1) / 2
    for i in first_indices:
        if first_indices[i] > 1:
            count += ((first_indices[i] * (first_indices[i] - 1)) / 2)

    if first_indices.get(0):
        count += first_indices.get(0)

    return int(count)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(valid_subarrays(arr, N))
