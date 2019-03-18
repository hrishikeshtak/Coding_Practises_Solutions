#!/usr/bin/env python3

# Symmetric Difference

# Given 2 sets of integers, M and N, print their symmetric difference
# in ascending order. The term symmetric difference indicates those
# values that exist in either M or N but do not exist in both.

M = int(input())
M_set = input()
M_set = set(map(int, M_set.split()))
N = int(input())
N_set = input()
N_set = set(map(int, N_set.split()))

# res1 = M_set.difference(N_set)
# res2 = N_set.difference(M_set)
# # symmetric difference
# res = res1.union(res2)

res = list(M_set.symmetric_difference(N_set))
res.sort()
print('\n'.join(map(str, res)))
