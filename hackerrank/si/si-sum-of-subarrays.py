#!/usr/bin/python3

# store subarray sum
subarray_sum = dict()


def find_subarray_sum(arr, i, j):
    global subarray_sum
    if i == 0:
        return subarray_sum[j]
    else:
        return subarray_sum[j] - subarray_sum[i-1]


def store_subarray_sum(arr, N):
    global subarray_sum
    total = 0
    for i in range(0, N):
        total += arr[i]
        subarray_sum[i] = total


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    store_subarray_sum(arr, N)
    # print(subarray_sum)
    for _ in range(int(input())):
        i, j = map(int, input().split())
        print(find_subarray_sum(arr, i, j))
