#!/usr/bin/python3

vowels = ["A", "O", "Y", "E", "U", "I"]

word = input()
result = ""
for char in word:
    if char.upper() not in vowels:
        result += "." + char.lower()
print(result)
