#!/usr/bin/python3

# Fn = {[(√5 + 1)/2] ^ n} / √5
from math import sqrt, pow

M = int(1e9+7)


# def pow(a, b):
#     x = a
#     ans = 1
#     while b != 0:
#         if b & 1:
#             ans = ((ans % M) * (x % M)) % M
#         x = ((x % M) * (x % M)) % M
#         b >>= 1
#     return ans


def fibo(N):
    if N <= 1:
        return 1

    fn = (1 + sqrt(5)) / 2
    N += 1
    return round((pow(fn, N) % M) / sqrt(5))


if __name__ == '__main__':
    for _ in range(int(input())):
        print(fibo(int(input())))
