#!/usr/bin/python3

# Prime or not Prime

# Input Format

# The first line contains an integer, T, the number of test cases.
# Each of the  subsequent lines contains an integer, , to be tested for
# primality.

# Constraints

# Output Format

# For each test case, print whether  is  or  on a new line.

# Sample Input

# 3
# 12
# 5
# 7
# Sample Output

# Not prime
# Prime
# Prime

import math


def checkPrime(num):
    if num == 1:
        return("Not prime")
    sqrt_n = int(math.sqrt(num))
    for i in range(2, sqrt_n + 1):
        if num % i == 0:
            return("Not prime")
    return("Prime")


T = int(input())
for i in range(T):
    num = int(input())
    print(checkPrime(num))
