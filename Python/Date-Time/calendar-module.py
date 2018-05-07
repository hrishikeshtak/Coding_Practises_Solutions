#!/usr/bin/env python3

# Calendar Module
# The calendar module allows you to output calendars and provides additional
# useful functions for them.

# Task

# You are given a date. Your task is to find what the day is on that date.

# Input Format

# A single line of input containing the space separated month, day and year,
# respectively, in MM DD YYYY format.

# Output Format

# Output the correct day in capital letters.

# Sample Input

# 08 05 2015
# Sample Output

# WEDNESDAY

import datetime
day = input()
print(datetime.datetime.strptime(day, "%m %d %Y").strftime('%A').upper())
