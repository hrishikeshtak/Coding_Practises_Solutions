#!/usr/bin/python3

"""
Given an array of size N and a number d, rotate the array to the left by d
i.e. shift the array elements to the left by d.
Ex: The array [1, 2, 3, 4, 5] after rotating by 2 gives [3, 4, 5, 1, 2].
"""

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    res = a[d:] + a[:d]
    print(*res)
