#!/usr/bin/python3

# Day 8: Dictionaries and Maps

# Task
# Given N names and phone numbers, assemble a phone book that maps friends'
# names to their respective phone numbers. You will then be
# given an unknown number of names to query your phone book for; for each
# queried, print the associated entry from your phone book (in
# the form name = phoneNumber) or Not found if there is no entry for name.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Input Format
# The first line contains an integer, N, denoting the number of entries in the
# phone book.
# Each of the N subsequent lines describes an entry in the form of 2
# space-separated values on a single line. The first value is a
# friend's name, and the second value is an 8-digit phone number.

# After the N lines of phone book entries, there are an unknown number of lines
# of queries. Each line (query) contains a name to look
# up, and you must continue reading lines until there is no more input.

# Note: Names consist of lowercase English letters and are first names only.

# Constraints
# 1 <= N <= 10^5
# 1 <= queries <= 10^5

# Output Format
# On a new line for each query, print Not found if the name has no
# corresponding entry in the phone book; otherwise, print the full
# name and phoneNumber in the format name = phoneNumber.

import sys


class Solution(object):
    """ provide dictionary map """
    def phonebook(self, phonebook, name):
        if name in phonebook:
            msg = name + "=" + str(phonebook[name])
            print(msg)
        else:
            print("Not found")


if __name__ == '__main__':
    n = input()
    phonebook = {}
    for i in range(int(n)):
        entry = input()
        # split name and number as key value pair
        try:
            name = entry.split()[0]
            number = int(entry.split()[1])
        except ValueError:
            print("Error: second value should be 8-digit phone number.\n")
            raise

        if isinstance(number, int):
            phonebook[name] = number
        else:
            raise Exception("second value should be 8-digit phone number.")
    while True:
        name = input()
        if not name:
            sys.exit()
        obj = Solution()
        obj.phonebook(phonebook, name)
