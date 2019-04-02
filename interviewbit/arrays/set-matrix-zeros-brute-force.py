#!/usr/bin/python3
"""
Given an m x n matrix of 0s and 1s, if an element is 0,
set its entire row and column to 0.
"""
# Complexity : O(N * M), O(N + M)


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        N = len(A)
        M = len(A[0])
        rows = []
        cols = []
        for i in range(0, N):
            for j in range(0, M):
                if A[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        # print(rows)
        # print(cols)
        for i in range(0, N):
            for j in range(0, M):
                if i in rows or j in cols:
                    A[i][j] = 0
        return A


def display(A):
    N = len(A)
    M = len(A[0])
    for i in range(0, N):
        for j in range(0, M):
            print(A[i][j], end=" ")
        print()


if __name__ == '__main__':
    A = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    display(A)
    A = Solution().setZeroes(A)
    display(A)
