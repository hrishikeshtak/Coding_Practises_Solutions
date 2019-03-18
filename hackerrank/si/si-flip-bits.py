#!/usr/bin/python3


def check_set_bits(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count


for _ in range(int(input())):
    x, y = map(int, input().split())
    print(check_set_bits(x ^ y))
