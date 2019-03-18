#!/usr/bin/env python3

import sys

# Task
# You have a non-empty set s, and you have to execute N commands
# given in N lines.

# The commands will be pop, remove and discard.

# Input Format

# The first line contains integer n, the number of elements in the set s.
# The second line contains  space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next  lines contains either pop, remove and/or discard commands
# followed by their associated value.

# Output Format

# Print the sum of the elements of set  on a single line

# Sample Input

# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

# Sample Output

# 4
n = int(input())
s = set(map(int, input().split()))
N = int(input())


for i in range(N):
    try:
        operation = input()
        command = operation.split()[0]
        if command == 'pop':
            temp = s.pop()
            continue
        value = int(operation.split()[1])
        if command == 'remove':
            s.remove(value)
        elif command == 'discard':
            s.discard(value)
    except Exception as err:
        print(err)
        sys.exit(0)
print(sum(s))
