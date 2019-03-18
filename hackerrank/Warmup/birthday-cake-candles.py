#!/bin/python3


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    return ar.count(max(ar))


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
