#!/bin/python


def aVeryBigSum(n, ar):
    # Complete this function
    result = 0
    for i in range(0, n):
        result += ar[i]
    return result


n = int(input().strip())
ar = map(int, input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
