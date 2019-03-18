#!/usr/bin/python3

from functools import reduce


def repeated_numbers(arr, N):
    xor = reduce(lambda x, y: x ^ y, arr)
    for i in range(1, N-1):
        xor ^= i

    # this will contains only set bits of repeated numbers
    set_bit_number = xor & ~(xor - 1)
    # print("set_bit_number: ", set_bit_number)
    # print("xor2: ", xor2)
    x = 0
    y = 0
    # xor with xor2 and those who are having set bits from arr
    for i in arr:
        if i & set_bit_number:
            x ^= i
        else:
            y ^= i
    for i in range(1, N-1):
        if i & set_bit_number:
            x ^= i
        else:
            y ^= i
    return(x, y)


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        x, y = repeated_numbers(arr, N)
        if x < y:
            print(x, y)
        else:
            print(y, x)
