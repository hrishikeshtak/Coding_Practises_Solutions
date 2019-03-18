#!/usr/bin/python3

n = int(input())
arr = list(map(int, input().split()))
if sum(arr) % 4 == 0:
    print(sum(arr) // 4)
else:
    print((sum(arr) // 4) + 1)
