#!/usr/bin/python3

x = 0
for _ in range(int(input())):
    op = input()
    if '++' in op:
        x += 1
    elif '--' in op:
        x -= 1
print(x)
