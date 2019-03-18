#!/usr/bin/python3

import math


def divisors(N):
    count = 0
    i = 1
    while i <= math.sqrt(N):
        if (N % i) == 0:
            if N / i == i:
                count += 1
            else:
                count += 2
        i += 1
    return count


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(divisors(N))
