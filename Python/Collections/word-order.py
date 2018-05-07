#!/usr/bin/env python3

# word-order

# You are given n words. Some words may repeat. For each word,
# output its number of occurrences. The output order should correspond
# with the input order of appearance of the word. See the sample input/output
# for clarification.

# Note: Each input line ends with a "\n" character.

# Input Format

# The first line contains the integer, n.
# The next n lines each contain a word.

# Output Format

# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct
# word according to their appearance in the input.

# Sample Input

# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output

# 3
# 2 1 1

from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words.keys()))
print(*words.values())
