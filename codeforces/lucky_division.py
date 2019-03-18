#!/usr/bin/python3

n = int(input())

lucky_number = [4, 7]
if n % 4 == 0 or n % 7 == 0 or n in lucky_number:
    print("YES")
else:
    for digit in str(n):
        if int(digit) not in lucky_number:
            print("NO")
    print("YES")
