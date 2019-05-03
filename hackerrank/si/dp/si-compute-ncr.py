#!/usr/bin/python3

M = int(1e9 + 7)
R = 2000
N = 2000
dp = [[0 for i in range(R+1)] for j in range(N+1)]


def store_ncr():
    global dp
    dp = [[0 for i in range(R+1)] for j in range(N+1)]

    # base condition, initialize 1st col
    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        for j in range(1, R+1):
            dp[i][j] = ((dp[i-1][j]) % M + (dp[i-1][j-1]) % M) % M


def compute_ncr(A, B):
    if B == 1:
        return A

    return dp[A][B]


if __name__ == '__main__':
    store_ncr()
    for _ in range(int(input())):
        A, B = map(int, input().split())
        print(compute_ncr(A, B))
