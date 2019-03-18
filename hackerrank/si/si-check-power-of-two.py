#!/usr/bin/python3


def check_power_of_two(n):
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1

    return True if count == 1 else False


for _ in range(int(input())):
    n = int(input())
    print(check_power_of_two(n))
