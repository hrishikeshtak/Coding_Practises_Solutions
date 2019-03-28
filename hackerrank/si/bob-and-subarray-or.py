#!/usr/bin/python3

# Compute the sum of the Bitwise OR of all the subarrays present in the array.


def subarray_OR_sum(arr, n):
    ans = 0
    for bit in range(0, 32):
        c = 0
        for i in range(0, n):
            if (arr[i] >> bit) & 1:
                ans += (n - i) * (1 << bit) * (c + 1)
                c = 0
            else:
                c += 1
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(subarray_OR_sum(arr, n))
