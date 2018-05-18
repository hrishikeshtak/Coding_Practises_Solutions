#!/usr/bin/python3


# Task
# Consider a database table, Emails, which has the attributes First Name and
# Email ID. Given N rows of data simulating the Emails table, print an
# alphabetically-ordered list of people whose email address ends in
# @gmail.com.

# Input Format

# The first line contains an integer, N, total number of rows in the table.
# Each of the N subsequent lines contains 2 space-separated strings denoting
# a person's first name and email ID, respectively.

# Output Format

# Print an alphabetically-ordered list of first names for every user with a
# gmail account. Each name must be printed on a new line.

# Sample Input

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com
# Sample Output

# julia
# julia
# riya
# samantha
# tanya


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    firstNames = list()
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID.endswith('@gmail.com'):
            firstNames.append(firstName)
    firstNames.sort()
    for name in firstNames:
        print(name)
