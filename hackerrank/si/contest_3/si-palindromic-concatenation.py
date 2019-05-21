#!/usr/bin/python3

from collections import defaultdict


def check_palindrome_substring(A, B):
    if A == B:
        return True

    # maintain hash table
    hash_table = defaultdict(int)
    for i in A:
        hash_table[i] += 1
    # print(hash_table)

    for i in B:
        if hash_table[i] >= 1:
            return True
    return False


if __name__ == '__main__':
    for _ in range(int(input())):
        A, B = input().split()
        status = check_palindrome_substring(A, B)
        if status:
            print("Yes")
        else:
            print("No")
