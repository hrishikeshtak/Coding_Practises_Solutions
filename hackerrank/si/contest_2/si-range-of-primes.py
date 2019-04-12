#!/usr/bin/python3

# print all prime numbers from 1 to N
SIZE = int(1e6)
# To store prime count till no
PRIME_COUNT = [0] * (SIZE + 1)


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
    global PRIME_COUNT
    PRIMES = [True] * (SIZE + 1)
    # primes = [True] * (N + 1)
    PRIMES[0] = PRIMES[1] = False

    for i in range(2, sqrt(N) + 1):
        if PRIMES[i]:
            PRIME_COUNT[i] = PRIME_COUNT[i-1] + 1
            for j in range(i*i, N+1, i):
                PRIMES[j] = False
        else:
            PRIME_COUNT[i] = PRIME_COUNT[i-1]

    # To update count of remaining numbers
    for i in range(sqrt(N) + 1, N+1):
        if PRIMES[i]:
            PRIME_COUNT[i] = PRIME_COUNT[i-1] + 1
        else:
            PRIME_COUNT[i] = PRIME_COUNT[i-1]

    # print("Prime numbers: ", PRIMES)
    # print("Prime count: ", PRIME_COUNT)


def prime_range(A, B):
    return PRIME_COUNT[B] - PRIME_COUNT[A-1]


if __name__ == '__main__':
    sieve_primes(SIZE)
    for _ in range(int(input())):
        A, B = map(int, input().split())
        print(prime_range(A, B))
