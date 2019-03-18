#!/bin/python3


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total_sum = sum(arr)
    print(total_sum - max(arr), total_sum - min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
