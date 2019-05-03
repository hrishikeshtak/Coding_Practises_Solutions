#!/usr/bin/python3

M = int(1e9+7)
N = int(1e5)

dp = [0] * (N+1)


def store_ways():
    global dp
    dp[0] = 1

    for i in range(1, N+1):
        j = 1
        while (i - j >= 0) and j <= 6:
            dp[i] = ((dp[i]) % M + (dp[i-j]) % M) % M
            j += 1


def number_of_ways(N):
    return dp[N]


if __name__ == '__main__':
    store_ways()
    # print(dp)
    for _ in range(int(input())):
        N = int(input())
        print(number_of_ways(N))
