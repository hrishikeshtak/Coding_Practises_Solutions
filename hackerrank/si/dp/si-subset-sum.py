#!/usr/bin/python3


def subset_sum(arr, N, K):
    dp = [[False for i in range(K+1)] for j in range(N+1)]

    # base condition, initialize 1st col with True
    for i in range(0, N+1):
        dp[i][0] = True

    for i in range(1, N+1):
        for j in range(1, K+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]


if __name__ == '__main__':
    for _ in range(int(input())):
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        status = subset_sum(arr, N, K)
        if status:
            print("YES")
        else:
            print("NO")
