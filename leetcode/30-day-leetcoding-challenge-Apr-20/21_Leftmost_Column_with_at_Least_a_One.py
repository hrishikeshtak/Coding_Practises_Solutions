#!/usr/bin/python3

"""
Leftmost Column with at Least a One
"""


# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat

    def get(self, x: int, y: int) -> int:
        return self.mat[x][y]

    def dimensions(self) -> 'list[]':
        n = len(self.mat)
        m = len(self.mat[0])

        return [n, m]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()

        if not binaryMatrix:
            return -1

        # points of top right corner
        i = 0
        j = m - 1

        ans = -1

        while i < n and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                ans = j
                j -= 1
            else:
                i += 1

        return ans


if __name__ == '__main__':
    mat = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    # mat = [[0,0],[0,0]]
    # mat = [[0,0],[0,1]]
    # mat = [[0,0],[1,1]]
    print(f"{Solution().leftMostColumnWithOne(mat)}")
