#!/bin/python3


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    primary_diagonal = 0
    secondary_diagonal = 0
    n = len(arr)
    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n-1-i]
    return abs(primary_diagonal - secondary_diagonal)


if __name__ == '__main__':
    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
