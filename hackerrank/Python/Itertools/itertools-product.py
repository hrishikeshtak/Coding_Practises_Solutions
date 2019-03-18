#!/usr/bin/env python3

# itertools.product()

# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Task

# You are given a two lists A and B.
# Your task is to compute their cartesian product A X B.

# Example

# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]

from itertools import product

A = list(map(int, input().split()))

B = list(map(int, input().split()))

for i in product(A, B):
    # space as delimiter in print statement
    print(i, end=' ')
