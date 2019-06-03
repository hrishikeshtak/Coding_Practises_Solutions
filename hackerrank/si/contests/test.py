#!/bin/python3

#
# Complete the 'lotteryCoupons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
from collections import defaultdict


def digitSum(n):
    ans = 0
    while n > 0:
        m = n % 10
        ans += m
        n = n // 10
    return ans


def lotteryCoupons(n):
    # prepare hashmap with (S, Count)
    hashmap = defaultdict(lambda: 0)

    for i in range(1, n+1):
        if i < 10:
            hashmap[i] += 1
        else:
            # combine number
            number = digitSum(i)
            hashmap[number] += 1
    # take max from values
    max_value = max(hashmap.values())
    return list(hashmap.values()).count(max_value)



if __name__ == '__main__':