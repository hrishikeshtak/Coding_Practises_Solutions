#!/usr/bin/python3

# Brute force O(N^2)


def valid_subarrays(arr, N):
    valid_subarray = 0
    for i in range(0, N+1):
        count = [0] * 2
        for j in range(i, N):
            # print(arr[j])
            # print(arr[i:j+1])
            count[arr[j]] += 1
            # print("count: ", count)
            if count[0] == count[1]:
                valid_subarray += 1

        # print(count)
    return valid_subarray


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(valid_subarrays(arr, N))
