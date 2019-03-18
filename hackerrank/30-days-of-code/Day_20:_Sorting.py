#!/usr/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numberOfSwaps = 0

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j] = a[j] + a[j+1]
            a[j+1] = a[j] - a[j+1]
            a[j] = a[j] - a[j+1]
            numberOfSwaps += 1

print("Array is sorted in %s swaps." % (numberOfSwaps))
print("First Element: %s" % (a[0]))
print("Last Element: %s" % (a[-1]))
