#!/usr/bin/python3


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, arr):
        # remove 0 at start
        A = []
        for i in arr:
            if i != 0:
                A.append(i)

        if not A:
            A = [0]

        A = A[::-1]
        s = 1
        c = 0
        for i in range(len(A)):
            s = A[i] + s + c
            if s == 10:
                s = 0
                c = 1
            else:
                c = 0
            A[i] = s
            if c == 0:
                s = 0

        if c == 1:
            A.append(1)

        return A[::-1]
