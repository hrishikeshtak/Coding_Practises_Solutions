#!/usr/bin/python3


def isEven(N):
    if N <= 2:
        return("No")
    if N & 1 == 0:
        return("Yes")
    else:
        return("No")


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        print(isEven(N))
