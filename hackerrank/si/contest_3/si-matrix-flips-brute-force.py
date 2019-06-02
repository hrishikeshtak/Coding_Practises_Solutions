#!/usr/bin/python3

"""
Given a grid of light bulbs - RxC, our goal is to turn on all the lights:
1 = on, 0 = off. Flipping a blub means changing its state: on to off, or off
to on. You can only perform the following operation any number of times:
Flip(i,j) - all the bulbs in the matrix occuring before (i,j) gets flipped.
"""


def matrix_flips(arr):
    # using floor and ceil logic
    # convert matrix to two list of 0's and 1's
    # store 0 and 1 value indices in separate list
    lst_0 = []
    lst_1 = []

    N = len(arr)
    # store 0 value indices
    for i in range(N):
        if arr[i] == '0':
            lst_0.append(i)

    # if lst_0 does not exist
    if not lst_0:
        return 0

    # store 1 value indices, till last 0th index
    for i in range(N):
        if arr[i] == '1' and i < lst_0[-1]:
            lst_1.append(i)

    flips = 0
    # do flips till lst_0 becomes empty
    while lst_0:
        # print("lst_0: ", lst_0)
        # print("lst_1: ", lst_1)

        # max index of 0th element
        max_0_index = lst_0.pop()
        flips += 1
        # find floor value of max_0_index in lst_1
        floor = find_floor(lst_1, max_0_index)
        # print("floor of {}: {}".format(max_0_index, floor))
        if floor == -1:
            break

        # after first 0, swap array of lst_0 and lst_1
        # indices of 1 becomes indices of 0

        # max index of 1 element
        max_1_index = lst_1.pop()
        flips += 1
        # find floor value of max_1_index in lst_0
        floor = find_floor(lst_0, max_1_index)
        # print("floor of {}: {}".format(max_1_index, floor))
        if floor == -1:
            break

    return flips


def find_floor(arr, X):
    lo = 0
    hi = len(arr) - 1

    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < X:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


if __name__ == '__main__':
    for _ in range(int(input())):
        R, C = map(int, input().split())
        arr = ""
        for _ in range(R):
            arr += (input())
        print(matrix_flips(arr))
