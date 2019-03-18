#!/usr/bin/env python3

# itertools.combinations_with_replacement(iterable, r)

# This tool returns r length subsequences of elements from the input iterable
# allowing individual elements to be repeated more than once.

# Combinations are emitted in lexicographic sorted order. So, if the input
# iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations_with_replacement

string, k = input().split()
iter_obj = combinations_with_replacement(sorted(string), int(k))
while True:
    try:
        print("".join(iter_obj.__next__()))
    except StopIteration:
        break
