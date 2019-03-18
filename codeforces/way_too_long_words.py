#!/usr/bin/python3

for _ in range(int(input())):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word[1:-1])) + word[-1])
