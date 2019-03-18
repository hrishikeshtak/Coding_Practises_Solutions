#!/bin/python3


# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1):
        stair = '#' * i
        print(stair.rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
