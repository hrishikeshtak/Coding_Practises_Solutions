#!/usr/bin/python3

# Optimize O(N)


def valid_subarrays(arr, N):
    first_indices = {}
    last_indices = {}
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

    # store first and last indices
    for i in range(0, N):
        if arr[i] in first_indices:
            last_indices[arr[i]] = i
        else:
            first_indices[arr[i]] = i
            last_indices[arr[i]] = i

    # print("first_indices: ", first_indices)
    # print("last_indices: ", last_indices)

    ans = 0
    # if only one element in hashmap, that means only one element
    # in array
    if len(first_indices) == 1:
        return ans

    for i in first_indices:
        ans += last_indices[i] - first_indices[i]
        # print(first_indices[i])
        # print(last_indices[i])

    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(valid_subarrays(arr, N))
