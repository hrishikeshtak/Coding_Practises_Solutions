#!/usr/bin/python3

# using hashing
from collections import defaultdict


def convertAnagrams(s1, s2):
    hashmap = defaultdict(lambda: 0)
    hashmap1 = defaultdict(lambda: 0)
    for i in range(0, len(s1)):
        hashmap[s1[i]] += 1
    # print(hashmap)

    for i in range(0, len(s2)):
        if hashmap[s2[i]] > 0:
            hashmap[s2[i]] -= 1
        else:
            hashmap1[s2[i]] += 1
    # print(hashmap)
    # print(hashmap1)

    cnt = 0
    for i in hashmap:
        # print(hashmap[i])
        if hashmap[i] > 0:
            cnt += hashmap[i]

    for i in hashmap1:
        # print(hashmap1[i])
        if hashmap1[i] > 0:
            cnt += hashmap1[i]
    return cnt


if __name__ == '__main__':
    for _ in range(int(input())):
        s1, s2 = input().split()
        print(convertAnagrams(s1, s2))
