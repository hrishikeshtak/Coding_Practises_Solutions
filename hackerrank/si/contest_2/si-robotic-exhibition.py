#!/usr/bin/python3

# Find the smallest positive integer value that cannot be represented as
# sum of any subset of a given array


def robotic_exhibition(arr, N):
    # Minimum number that can not be represented
    res = 1
    arr.sort()
    # print(arr)

    for i in range(0, N):
        # print(res, end=" ")
        if arr[i] <= res:
            res += arr[i]
        else:
            break
    # print()
    return res


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(robotic_exhibition(arr, N))
