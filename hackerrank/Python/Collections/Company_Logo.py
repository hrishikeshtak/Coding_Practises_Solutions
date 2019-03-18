#!/usr/bin/env python3

# Company Logo

# A newly opened multinational brand has decided to base their company logo
# on the three most common characters in the company name. They are now trying
# out various combinations of company names and logos based on this condition.
# Given a string s, which is the company name in lowercase letters,
# your task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical
# order.

# For example, according to the conditions described above,
# GOOGLE would have it's logo with the letters G, O, E.

# Input Format

# A single line of input containing the string S.

# Output Format

# Print the three most common characters along with their occurrence count
# each on a separate line.
# Sort output in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in
# alphabetical order.

# Sample Input 0

# aabbbccde
# Sample Output 0

# b 3
# a 2
# c 2


from collections import Counter
string = sorted(Counter(input()).items(), key=lambda x: (-x[-1], x[0]))[:3]
for element in string:
    print(" ".join(str(e) for e in element), sep=" ")
