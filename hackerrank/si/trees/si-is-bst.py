#!/usr/bin/python3

INT_MIN = -(1 << 31)
INT_MAX = (1 << 31) - 1


def LeftChildren(arr, idx):
    left = 2 * idx + 1
    return left


def RightChildren(arr, idx):
    right = 2 * idx + 2
    return right


def isBST(arr, idx, a, b, N):
    if not arr:
        return True

    if idx >= N:
        return True

    return arr[idx] > a and arr[idx] < b and \
        isBST(arr, LeftChildren(arr, idx), a, arr[idx], N) and \
        isBST(arr, RightChildren(arr, idx), arr[idx], b, N)


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        status = isBST(arr, 0, INT_MIN, INT_MAX, N)
        if status:
            print("True")
        else:
            print("False")
