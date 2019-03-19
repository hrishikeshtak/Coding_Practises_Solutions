#!/usr/bin/python3

# Optimal
"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order.
    (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, arr):
        repeated = dict()
        result = set()

        # print(arr)
        N = len(arr)
        if N < 3:
            return []
        # store negative of each element
        for i in range(N):
            if -arr[i] not in repeated:
                repeated[-arr[i]] = [i]
            else:
                repeated[-arr[i]].append(i)

        # print(repeated)
        for i in range(N-1):
            for j in range(i+1, N):
                if arr[i] + arr[j] in repeated:
                    for k in repeated[arr[i] + arr[j]]:
                        if k != i and k != j:
                            cur = sorted([arr[k], arr[i], arr[j]])
                            result.add(tuple(cur))

        return list(result)
