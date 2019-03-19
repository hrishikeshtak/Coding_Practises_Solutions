#!/usr/bin/python3

"""
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and
minimum number from the triplet a, b, c such that a, b, c belongs
arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]

Output:

1
"""

# Given arrays are already sorted.
# If not sorted then first sort the 3 arrays


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i = j = k = 0
        res = (1 << 31) - 1
        while i < len(A) and j < len(B) and k < len(C):
            # print("max: ", max(A[i], B[j], C[k]))
            # print("min: ", min(A[i], B[j], C[k]))
            res = min(res, abs((max(A[i], B[j], C[k]) - min(
                A[i], B[j], C[k]))))
            if A[i] <= B[j] and A[i] <= C[k]:
                i += 1
            elif B[j] <= A[i] and B[j] <= C[k]:
                j += 1
            else:
                k += 1
        return res
