#!/usr/bin/python3

# using hashing


def longest_subarray_with_sum_0(arr, N):
    """
    take prefix sum and store in hashmap.
    If cur sum exists in hashmap that means subarray make sum = 0
    """
    hashdict = dict()

    max_len = 0
    cur_sum = 0

    for i in range(0, N):
        cur_sum += arr[i]

        if arr[i] == 0 and max_len == 0:
            max_len = 1

        if cur_sum == 0:
            max_len = i + 1

        # store sum in hashmap
        if cur_sum in hashdict:
            max_len = max(max_len, i - hashdict[cur_sum])
        else:
            hashdict[cur_sum] = i
    return max_len


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(longest_subarray_with_sum_0(arr, N))
