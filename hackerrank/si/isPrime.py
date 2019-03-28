#!/usr/bin/python3


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


def isPrime(N):
    if N <= 1:
        return "False"
    # print(sqrt(N))
    for i in range(2, sqrt(N)):
        if N % i == 0:
            return "False"
    return "True"


if __name__ == '__main__':
    N = int(input())
    print(isPrime(N))
