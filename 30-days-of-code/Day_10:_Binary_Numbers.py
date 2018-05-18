#!/usr/bin/python3

# Day 10: Binary Numbers

# Task
# Given a base-10 integer, n, convert it to binary (base-2). Then find and
# print the base-10 integer denoting the maximum number of
# consecutive 1's in n's binary representation.

# Input Format
# A single integer, n.

# Constraints
# 1 <= n <= 10^6

# Output Format
# Print a single base-10 integer denoting the maximum number of consecutive
# 1's in the binary representation of n.

n = int(input().strip())
ans = 0
while n > 0:
    n &= (n << 1)
    ans += 1

print(ans)
