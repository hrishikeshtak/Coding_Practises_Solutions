#!/usr/bin/python3


M = int(1e9+7)
N = int(1e6)
dp = [0] * (N+1)


def store_dp():
    global dp0, dp1
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = (i * dp[i-1]) % M


def compute_factorial(N):
    return dp[N]


if __name__ == '__main__':
    store_dp()
    # print(dp)
    for _ in range(int(input())):
        N = int(input())
        print(compute_factorial(N))
