#!/usr/bin/python3


def isPalindrome(string):
    if string.lower() == string[::-1].lower():
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        string = input()
        isPalindrome(string)
