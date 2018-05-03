#!/usr/bin/env python3

# Check Subset

# Input Format

# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of
# set A
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of
# set B.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output

# True
# False
# False

# If set(A).difference(set(B)) is empty that means A is subset of B

T = int(input())

for i in range(T):
    n = int(input())
    A = set(map(int, input().split()[:n]))
    m = int(input())
    B = set(map(int, input().split()[:m]))
    if A.issubset(B):
        print(True)
    else:
        print(False)
