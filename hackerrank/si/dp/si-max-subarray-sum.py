#!/usr/bin/python3


def max_subarray_sum(arr, N):
    dp = [0] * (N+1)
    dp[0] = arr[0]

    for i in range(1, N):
        dp[i] = max(dp[i-1]+arr[i], 0)
    # print(dp)

    # ans is max from dp array
    x = y = 0
    j = k = 0
    ans = 0
    for i in range(0, N+1):
        if ans < dp[i]:
            k += 1
            y = i
            ans = max(ans, dp[i])
        if dp[i] == 0 and i <= y:
            x = i
    print(ans, x, y)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        max_subarray_sum(arr, N)
