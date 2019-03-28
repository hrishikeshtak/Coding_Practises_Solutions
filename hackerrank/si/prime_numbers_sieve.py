#!/usr/bin/python3

# print all prime numbers from 1 to N


def sqrt(N):
    ans = 1
    lo = 1
    hi = N
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= N:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def sieve_primes(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False

    for i in range(2, sqrt(N) + 1):
        if primes[i]:
            for j in range(i*i, N+1, i):
                primes[j] = False

    for i in range(0, N+1):
        if primes[i]:
            print(i, end=" ")


if __name__ == '__main__':
    N = int(input())
    sieve_primes(N)
    print()
