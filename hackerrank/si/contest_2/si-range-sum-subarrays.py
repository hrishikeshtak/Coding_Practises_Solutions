#!/usr/bin/python3

# Optimal : O(N)


def subarray_sum_less_K(arr, N, K):
    i = 0
    j = 0
    sub_sum = arr[0]
    cnt = 0

    while i < N and j < N:
        if sub_sum < K:
            j += 1

            if j >= i:
                cnt += j - i

            if j < N:
                sub_sum += arr[j]
        else:
            sub_sum -= arr[i]
            i += 1
    return cnt


def range_subarray(arr, N, A, B):
    B_cnt = subarray_sum_less_K(arr, N, B)
    A_cnt = subarray_sum_less_K(arr, N, A-1)
    print(B_cnt, A_cnt)
    return B_cnt - A_cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        N, A, B = map(int, input().split())
        arr = list(map(int, input().split()))
        print(range_subarray(arr, N, A, B))
