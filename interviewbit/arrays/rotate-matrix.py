#!/usr/bin/python3


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, arr):
        N = len(arr[0])
        for i in range(N//2):
            for j in range(i, N-i-1):
                temp = arr[i][j]
                arr[i][j] = arr[N-j-1][i]
                arr[N-j-1][i] = arr[N-i-1][N-j-1]
                arr[N-i-1][N-j-1] = arr[j][N-i-1]
                arr[j][N-i-1] = temp
        return arr
