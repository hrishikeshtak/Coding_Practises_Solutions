#!/usr/bin/python3


def max_non_adjacent_sum(arr, N):
    dp = [0] * (N+1)
    dp[0] = arr[0]
    if N == 1:
        return max(dp[0], 0)

    dp[1] = max(arr[1], arr[0])

    for i in range(2, N):
        dp[i] = max((arr[i] + max(dp[i-2], 0)), dp[i-1])
    # print(dp)
    return dp[N-1]


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(max_non_adjacent_sum(arr, N))
