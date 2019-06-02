#!/usr/bin/python3

"""
Given a grid of light bulbs - RxC, our goal is to turn on all the lights:
1 = on, 0 = off. Flipping a blub means changing its state: on to off, or off
to on. You can only perform the following operation any number of times:
Flip(i,j) - all the bulbs in the matrix occuring before (i,j) gets flipped.
"""


def matrix_flips(arr, R, C):
    ans = 0
    no_of_shifts = 0

    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if (int(arr[i][j]) + no_of_shifts) % 2 == 0:
                ans += 1
                no_of_shifts += 1
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        R, C = map(int, input().split())
        matrix = []
        for _ in range(R):
            matrix.append(input())
        print(matrix_flips(matrix, R, C))
