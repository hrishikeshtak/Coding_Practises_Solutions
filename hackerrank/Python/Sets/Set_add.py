#!/usr/bin/env python3
# Set .add()
# >>> s = set('HackerRank')
# >>> s.add('H')
# >>> print s
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# >>> print s.add('HackerRank')
# None
# >>> print s
# set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the
# total number of distinct country stamps in her collection. She asked for
# your help. You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.

# Sample Input

# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Sample Output

# 5

N = int(input())

country_stamps = set()

for i in range(N):
    country_stamps.add(input())

print(len(country_stamps))
