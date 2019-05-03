#!/usr/bin/python3

# Given an array of positive integers, find 2 elements such that their xor:
# a ^ b is maximum


class TrieNode:
    def __init__(self):
        self.c = [None] * 2


def find_maximum_bits(x, N):
    b = 0
    while x:
        b += 1
        x >>= 1
    return b


def checkBit(x, i):
    return (x >> i) & 1


def insert(root, x, b):
    cur = root
    for i in range(b-1, -1, -1):
        idx = 1 if checkBit(x, i) == 1 else 0
        if cur.c[idx] is None:
            cur.c[idx] = TrieNode()
        cur = cur.c[idx]
    return root


def query(root, x, b):
    cur = root
    ans = 0
    for i in range(b-1, -1, -1):
        idx = 1 if checkBit(x, i) == 1 else 0
        if cur.c[1-idx]:
            ans += (1 << i)
            cur = cur.c[1-idx]
        else:
            cur = cur.c[idx]
    return ans


def maximum_xor(arr, N):
    root = TrieNode()
    # find max no of bits in array
    bits = 0
    for i in range(0, N):
        bits = max(bits, find_maximum_bits(arr[i], N))
    # print("maximum no of bits: ", bits)
    for i in range(N):
        root = insert(root, arr[i], bits)

    ans = 0
    for i in range(N):
        ans = max(ans, query(root, arr[i], bits))
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        print(maximum_xor(arr, N))
