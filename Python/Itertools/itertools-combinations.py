#!/usr/bin/env python3

# itertools.combinations(iterable, r)
# This tool returns the r length subsequences of elements from the
# input iterable.

# Combinations are emitted in lexicographic sorted order. So,
# if the input iterable is sorted, the combination tuples will be
# produced in sorted order.

from itertools import combinations
string, k = input().split()
for i in range(1, int(k)+1):
    iter_obj = combinations(sorted(string), i)
    while True:
        try:
            print("".join(iter_obj.__next__()))
        except StopIteration:
            break
