#!/usr/bin/env python3

# You are asked to ensure that the first and last names of people begin
# with a capital letter in their passports. For example, alison heck should
# be capitalised correctly as Alison Heck.

# Sample Input
# chris alan
# hello   world  lol

# Sample Output
# Chris Alan
# Hello   World  Lol


def capitalize(string):
    result = []
    for i in range(len(string)):
        if i == 0:
            result.append(string[i].upper())
        elif string[i-1] == ' ':
            result.append(string[i].upper())
        else:
            result.append(string[i])
    return("".join(result))


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
