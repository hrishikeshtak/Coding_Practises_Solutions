#!/usr/bin/python3

M = int(1e9 + 7)
N = int(1e6)

dp = [0] * (N+1)


def store_tiles():
    global dp
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 5

    for i in range(5, N+1):
        dp[i] = (dp[i-1] + dp[i-2] + 8 * dp[i-5]) % M


def arranging_dominos(X):
    global dp, N

    # if X >= N:
    #     for i in range(N, X+1):
    #         dp.append(dp[i-1] + dp[i-2] + 8 * dp[i-5])
    #     N += (X + 1 - N)

    return dp[X] % M


if __name__ == '__main__':
    store_tiles()
    for _ in range(int(input())):
        X = int(input())
        print(arranging_dominos(X))
