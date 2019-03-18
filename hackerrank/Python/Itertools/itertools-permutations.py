#!/usr/bin/env python3

# itertools.permutations()

# itertools.permutations(iterable[, r])

# This tool returns successive r length permutations of elements in an
# iterable.

# If r is not specified or is None, then  defaults to the length of the
# iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input
# iterable is sorted, the Permutations tuples will be produced in a
# sorted order.

from itertools import permutations

string, k = input().split()

iter_obj = permutations(sorted(string), int(k))
while True:
    try:
        print("".join(iter_obj.__next__()))
    except StopIteration:
        break

# for i in permutations(sorted(string), int(k)):
#     print("".join(i))
