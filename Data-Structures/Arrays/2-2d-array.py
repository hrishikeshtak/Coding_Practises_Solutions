#!/usr/bin/python3

# Context
# Given a 6 x 6 2D Array, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in
# this pattern in A's graphical representation:

# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an
# hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in A, then print the
# maximum hourglass sum.

# Input Format
# There are 6 lines of input, where each line contains 6 space-separated
# integers describing 2D Array A; every value in A will be in the
# inclusive range of -9 to 9.

# Constraints
# -9 <= A[i][j] <= 9
# 0 <= i,j <= 5

# Output Format
# Print the largest (maximum) hourglass sum found in A.

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output

# 19

import math
import os
import random
import re
import sys


# Complete the array2D function below.
def array2D(arr):
    res = list()
    for i in range(4):
        for j in range(4):
            result = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(
                arr[i+2][j:j+3])
            res.append(result)
    return(max(res))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
