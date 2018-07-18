#!/usr/bin/python3

N = int(input())

stack = [0]

for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    if line[0] == 1:
        stack.append(max(line[1], stack[-1]))
    elif line[0] == 2:
        stack.pop()
    elif line[0] == 3:
        print(stack[-1])
