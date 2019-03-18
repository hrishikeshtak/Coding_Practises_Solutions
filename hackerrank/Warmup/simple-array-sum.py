#!/usr/bin/python3

from functools import reduce


def simpleArraySum(n, ar):
    # Complete this function
    return reduce(lambda x, y: x + y, ar)


n = int(input().strip())
ar = map(int, input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
