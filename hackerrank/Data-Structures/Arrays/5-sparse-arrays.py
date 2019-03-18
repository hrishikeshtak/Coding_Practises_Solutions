#!/usr/bin/python3


from collections import defaultdict


if __name__ == '__main__':
    strings_count = int(input())
    strings = defaultdict(int)
    for _ in range(strings_count):
        strings[input()] += 1

    queries_count = int(input())
    for _ in range(queries_count):
        print(strings[input()])
