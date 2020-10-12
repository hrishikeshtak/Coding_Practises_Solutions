#!/usr/bin/python3

"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return
whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.
"""


def pair_sum(arr, K):
    hashset = set()
    for i in range(0, len(arr)):
        if K - arr[i] in hashset:
            return "True"
        else:
            hashset.add(arr[i])
    return "False"


arr = [-10, -15, 3, 7]
K = -25
print(pair_sum(arr, K))
