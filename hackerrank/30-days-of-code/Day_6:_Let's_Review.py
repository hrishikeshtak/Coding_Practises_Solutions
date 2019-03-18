#!/usr/bin/python3

# Task
# Given a string, S, of length N that is indexed from 0 to N-1, print
# its even-indexed and odd-indexed characters as 2 space-separated
# strings on a single line (see the Sample below for more detail).

# Note: 0 is considered to be an even index.

# Input Format
# The first line contains an integer, T (the number of test cases).
# Each line i of the T subsequent lines contain a String, S.

# Constraints
# 1 <= T <= 10
# 2 <= length of S <= 10000

# Output Format
# For each String Sj (where 0 <= j <= T - 1), print Sj's even-indexed
# characters, followed by a space, followed by Sj's odd-indexed characters.

T = int(input())

for i in range(0, T):
    even_string = []
    odd_string = []
    S = input()
    for j in range(len(S)):
        if j % 2 == 0:
            even_string.append(S[j])
        else:
            odd_string.append(S[j])
    print(''.join(even_string) + " " + ''.join(odd_string))
