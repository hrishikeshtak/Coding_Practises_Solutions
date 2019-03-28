#!/usr/bin/python3


def sqrt(N):
    lo = 1
    hi = N
    ans = 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= N:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


def divisor_summation(N):
    # print(sqrt(N))
    count = 0
    divisors = set()
    for i in range(1, sqrt(N) + 1):
        if N % i == 0:
            if N / i == i:
                divisors.add(i)
                count += 1
            else:
                divisors.add(i)
                divisors.add(N//i)
                count += 2

    # print(divisors)
    return (sum(divisors) - N)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        print(divisor_summation(N))
