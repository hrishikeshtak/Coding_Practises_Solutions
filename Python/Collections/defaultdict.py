#!/usr/bin/env python3

# DefaultDict Tutorial

# The defaultdict tool is a container in the collections class of Python.
# It's similar to the usual dictionary (dict) container, but it has one
# difference: The value fields' data type is specified upon initialization.

# In this challenge, you will be given 2 integers, n and m.
# There are n words, which might repeat, in word group A.
# There are m words belonging to word group B. For each m words,
# check whether the word has appeared in group A or not.
# Print the indices of each occurrence of m in group A.
# If it does not appear, print -1.

# Input Format

# The first line contains integers, n and m separated by a space.
# The next n lines contains the words belonging to group A.
# The next m lines contains the words belonging to group B.

# Output Format

# Output  lines.
# The ith line should contain the 1-indexed positions of the occurrences of
# the ith word separated by spaces.

# Sample Input

# 5 2
# a
# a
# b
# a
# b
# a
# b
# Sample Output

# 1 2 4
# 3 5

from collections import defaultdict

n, m = map(int, input().split())

# initialize default dict with -1
words_dict = defaultdict(lambda: -1)

for i in range(1, n + 1):
    word = input()
    words_dict[word] = words_dict[word] + ' ' + \
        str(i) if word in words_dict else str(i)

for _ in range(m):
    print(words_dict[input()])
