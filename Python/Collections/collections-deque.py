#!/usr/bin/env python3

# collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements
# from both ends.
# Deques support thread safe, memory efficient appends and pops from
# either side of the deque with approximately the same O(1) performance in
# either direction.

# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format

# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their
# values.

# Output Format

# Print the space separated elements of deque .

from collections import deque

d = deque()
# getattr : Get a named attribute from an object; getattr(x, 'y') is
# equivalent to x.y.
for _ in range(int(input())):
    inp = input().split()
    getattr(d, inp[0])(*[int(inp[1])] if len(inp) > 1 else [])
print(*[item for item in d])
