#!/usr/bin/python3

from math import sqrt

M = int(1e8)
PRIMES = [True] * (M+1)
# PRIME_NUMBER = []


def sieve_prime():
    """Store Prime numbers upto 1e6"""
    global PRIMES
    PRIMES[0] = PRIMES[1] = False

    for i in range(2, int(sqrt(M)) + 1):
        if PRIMES[i]:
            for j in range(i*i, M+1, i):
                PRIMES[j] = False

    # for i in range(len(PRIMES)):
    #     if PRIMES[i]:
    #         PRIME_NUMBER.append(i)
            # print(i, end=" ")
    # print()
    # print(PRIME_NUMBER)


def find_kth_prime(N):
    j = 0
    for i in range(0, M):
        if PRIMES[i]:
            j += 1
            if j == N:
                return i
    # return PRIME_NUMBER[N-1]


if __name__ == '__main__':
    sieve_prime()
    # print(PRIMES)
    for _ in range(int(input())):
        N = int(input())
        print(find_kth_prime(N))
