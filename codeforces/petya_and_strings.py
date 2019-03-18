#!/usr/bin/python3

str1 = input()
str2 = input()

if str1.lower() == str2.lower():
    print(0)
elif str1.lower() < str2.lower():
    print(-1)
else:
    print(1)
