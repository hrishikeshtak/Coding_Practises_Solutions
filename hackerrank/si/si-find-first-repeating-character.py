#!/usr/bin/python3

from collections import defaultdict


def repeating_char(string):
    hashmap = defaultdict(lambda: 0)
    for char in string:
        hashmap[char.lower()] += 1

    for char in string:
        if hashmap[char.lower()] > 1:
            return char
    return '.'


for _ in range(int(input())):
    string = input()
    print(repeating_char(string))
