#!/usr/bin/python3

# Given two numbers a and b, you have to find n-th
# number which is divisible by a or b.


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def divTermCount(a, b, mid):
    lcm = (a * b) // gcd(a, b)
    # print("lcm: %s, gcd: %s" % (lcm, gcd(a, b)))
    # Total no divisible by a and b not by both
    try:
        terms = (mid // a) + (mid // b) - (mid // lcm)
    except ZeroDivisionError:
        terms = 0
    return terms


def findNthTerm(a, b, n):
    lo = 0
    hi = max(a, b) * n
    while lo < hi:
        mid = (lo + hi) // 2
        # print("lo: %s, mid: %s, hi: %s" % (lo, mid, hi))
        if divTermCount(a, b, mid) < n:
            # ans = mid
            lo = mid + 1
        else:
            hi = mid
    return lo
    # print(lo)
    # print()


if __name__ == '__main__':
    try:
        for _ in range(int(input())):
            a, b, n = map(int, input().split())
            # print(a, b)
            ans = findNthTerm(a, b, n)
            print(ans)
    except Exception:
        print(ans)
