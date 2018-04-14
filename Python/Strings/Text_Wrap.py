#!/usr/bin/env python3

# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width .

# Input Format

# The first line contains a string, S.
# The second line contains the width, w.

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap


def wrap(string, max_width):
    return("\n".join(textwrap.wrap(string, max_width)))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
