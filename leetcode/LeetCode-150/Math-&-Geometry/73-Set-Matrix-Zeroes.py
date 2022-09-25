"""
73. Set Matrix Zeroes
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        row_zero, col_zero = set(), set()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero.add(i)
                    col_zero.add(j)
        for i in range(rows):
            for j in range(cols):
                if i in row_zero or j in col_zero:
                    matrix[i][j] = 0
