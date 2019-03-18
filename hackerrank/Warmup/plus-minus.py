#!/bin/python3


# Complete the plusMinus function below.
def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1

    print("{:.6f}".format(positive_count / len(arr)))
    print("{:.6f}".format(negative_count / len(arr)))
    print("{:.6f}".format(zero_count / len(arr)))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
