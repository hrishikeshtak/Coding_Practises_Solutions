#!/usr/bin/python3

word = input()
new_word = ""
for char in word:
    if char in "hello":
        new_word += char

# print(new_word)
hello = "hello"
i = 0
j = 0
while i != len(hello) and j != len(new_word):
    if hello[i] == new_word[j]:
        i += 1
        j += 1
    else:
        j += 1

if i == len(hello):
    print("YES")
else:
    print("NO")
