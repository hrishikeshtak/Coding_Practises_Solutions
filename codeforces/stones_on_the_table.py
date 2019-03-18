#!/usr/bin/python3

n = int(input())
stone = input()
count = 0

for i in range(n-1):
    if stone[i] == stone[i+1]:
        count += 1
print(count)
