#!/usr/bin/env python3

# No Idea!

# There is an array of n integers. There are also 2 disjoint sets,
# A and B, each containing m integers. You like all the integers in set
# A and dislike all the integers in set B.
# Your initial happiness is 0. For each i integer in the array, if i E A,
# you add 1 to your happiness,. If i E B, you add -1 to your happiness.
# Otherwise,
# your happiness does not change. Output your final happiness at the end.

# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1

n, m = map(int, input().split())

array = list(map(int, input().split()[:n]))

# [:n] accepts only n integers

A = set(map(int, input().split()[:m]))
B = set(map(int, input().split()[:m]))

happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1

print(happiness)
