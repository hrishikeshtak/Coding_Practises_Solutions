#!/usr/bin/python3

"""
You’re given a read only array of n integers. Find out if any integer
occurs more than n/3 times in the array in linear time and constant
additional space.

If so, return the integer. If not, return -1.
"""

from collections import defaultdict


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        N = len(A)
        hashmap = defaultdict(lambda: 0)
        for i in range(0, N):
            hashmap[A[i]] += 1
        # print(hashmap)
        for i in range(0, N):
            if hashmap[A[i]] > N//3:
                return A[i]
        return -1


if __name__ == '__main__':
    A = [1, 2, 3, 1, 1]
    print(Solution().repeatedNumber(A))
