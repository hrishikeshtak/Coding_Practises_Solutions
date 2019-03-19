#!/usr/bin/python3

"""
Given an array of N integers, find the pair of integers in the array which
have minimum XOR value. Report the minimum XOR value.
"""


class Solution:
    # @param A : list of integers
    # @return an integer

    def findMinXor(self, A):
        n = len(A)
        A.sort()
        min_xor = A[-1]
        for i in range(n-1):
            val = A[i] ^ A[i+1]
            min_xor = min(min_xor, val)

        return min_xor
