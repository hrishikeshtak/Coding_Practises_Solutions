#!/usr/bin/python3
INT_MIN = -(1 << 31)

# O(N**2)


def max_subarray_sum(arr, N):
    ans = INT_MIN
    for i in range(0, N):
        sub_sum = 0
        for j in range(i, N):
            sub_sum += arr[j]
            ans = max(ans, sub_sum)
    return ans


if __name__ == '__main__':
    arr = [5, 4, -10, 6, 10, -3, 4, -1, 5, 2, -25, 10, 4, 1, 2, -5, 3]
    print(max_subarray_sum(arr, len(arr)))
