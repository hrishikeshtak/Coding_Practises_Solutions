#!/usr/bin/python3


M = int(1e9+7)
N = int(1e5)
dp0 = [0] * (N+1)
dp1 = [0] * (N+1)


def store_dp():
    global dp0, dp1
    dp0[0] = 1
    dp0[1] = 1
    dp1[0] = 1
    dp1[1] = 1

    for i in range(2, N+1):
        dp0[i] = (dp0[i-1]) + (dp1[i-1])
        dp1[i] = (dp0[i-1])


def binary_strings_with_no_adjacent_1s(N):
    return (dp0[N] + dp1[N]) % M


if __name__ == '__main__':
    store_dp()
    for _ in range(int(input())):
        N = int(input())
        print(binary_strings_with_no_adjacent_1s(N))
