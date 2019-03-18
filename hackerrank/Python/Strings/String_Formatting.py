#!/usr/bin/env python3

# Given an integer, b, print the following values for each integer i
# from 1 to n:

# 1 Decimal
# 2 Octal
# 3 Hexadecimal (capitalized)
# 4 Binary

# The four values must be printed on a single line in
# the order specified above for each i from 1 to n.
# Each value should be space-padded to match the width of the binary value of n


def print_formatted(number):
    # your code goes here
    for i in range(1, n+1):
        print("%d %s %s %s" % (
            i,
            oct(i).split('0o')[-1],
            hex(i).split('0x')[-1].capitalize(),
            bin(i).split('0b')[-1]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
