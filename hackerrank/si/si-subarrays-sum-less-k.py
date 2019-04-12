#!/usr/bin/python3


def subarray_with_sum_less_k(arr, N, K):
    cnt = 0
    sub_sum = arr[0]
    i = 0
    j = 0
    while i < N and j < N:
        if sub_sum <= K:
            j += 1

            if j >= i:
                cnt += j - i

            if j < N:
                sub_sum += arr[j]
        else:
            sub_sum -= arr[i]
            i += 1
    return cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        print(subarray_with_sum_less_k(arr, N, K))
