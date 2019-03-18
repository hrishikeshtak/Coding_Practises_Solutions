#!/usr/bin/python3

string = input()
numbers = string.split('+')
numbers.sort()
print("+".join(numbers))
