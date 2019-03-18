#!/usr/bin/env python3

import sys
# Check Strict Superset

# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the n sets.

# Print True, if A is a strict superset of each of the n sets.
# Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

A = set(map(int, input().split()))

n = int(input())

for i in range(n):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        print(False)
        sys.exit(0)
print(True)
