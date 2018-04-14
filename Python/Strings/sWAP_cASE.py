#!/usr/bin/python3

import string

# sWAP cASE

# You are given a string S. Your task is to swap cases.
# In other words, convert all lowercase letters to uppercase
# letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

# Input Format
# A single line containing a string S.

# Constraints
# 0 < len(S) <= 1000

# Output Format
# Print the modified string S.


def swap_case(s):
    """ swap case: lower to upper and vice-versa
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    result = []
    for char in s:
        if char in lowercase:
            result.append(char.upper())
        elif char in uppercase:
            result.append(char.lower())
        else:
            result.append(char)
    return(''.join(result))


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
