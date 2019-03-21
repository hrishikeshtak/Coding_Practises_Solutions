#!/usr/bin/python3

# using hashing
from collections import defaultdict


def isAnagram(s1, s2):
    hashmap = defaultdict(lambda: 0)
    for i in range(0, len(s1)):
        hashmap[s1[i]] += 1
    # print(hashmap)
    for i in range(0, len(s2)):
        hashmap[s2[i]] -= 1
    # print(hashmap)

    # chech hashmap having all values 0
    for key, value in hashmap.items():
        if value != 0:
            return "False"
    return "True"


if __name__ == '__main__':
    for _ in range(int(input())):
        s1, s2 = input().split()
        print(isAnagram(s1, s2))
