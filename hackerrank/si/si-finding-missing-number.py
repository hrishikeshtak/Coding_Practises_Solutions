#!/usr/bin/python3

from functools import reduce

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr_xor = reduce(lambda x, y: x ^ y, arr)
    sequence_xor = reduce(lambda x, y: x ^ y, range(1, n+2))

    print(arr_xor ^ sequence_xor)
