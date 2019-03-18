#!/usr/bin/python3


def bin_representation(n):
    if (n > 1):
        bin_representation(n >> 1)
    print(n & 1, end="")


for _ in range(int(input())):
    n = int(input())
    bin_representation(n)
    print()
