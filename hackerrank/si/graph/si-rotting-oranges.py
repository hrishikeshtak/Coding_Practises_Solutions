#!/usr/bin/python3

from collections import deque

"""
You are given a 2D matrix consisting of oranges.
mat[i][j] = 0: Empty cell
mat[i][j] = 1: Fresh Orange
mat[i][j] = 2: Rotten Orange

As a matter of fact, the rotten oranges spread to the neighbouring cells
and rot the fresh oranges. Assuming it takes 1 day for a rotten orange to
spread to a neighbouring fresh orange, find out the minimum number of days
in which all the oranges rot out. If there is atleast 1 fresh orange which
will never rot, print -1.
"""


def valid(i, j, N):
    if i < 0 or j < 0 or i >= N or j >= N:
        return False
    return True


def rotten_oranges(mat, N):
    """Use BFS Traversal."""
    # create Q to store indices of rotten oranges

    Q = deque()  # rotten oranges indices
    F = []  # Fresh oranges indices

    # store indices of fresh and rotten oranges
    for i in range(0, N):
        for j in range(0, N):
            if mat[i][j] == 2:
                Q.append((i, j))
            elif mat[i][j] == 1:
                F.append((i, j))

    # append None to identify timelapse
    Q.append(None)

    # N-4 neighbours
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    time = 0
    while len(Q) > 1:
        temp = Q.popleft()
        if temp:
            x, y = temp
            # rotten the N-4 fresh oranges
            for k in range(0, 4):
                i = x + di[k]
                j = y + dj[k]
                if valid(i, j, N) and mat[i][j] == 1:
                    mat[i][j] = 2
                    Q.append((i, j))
        else:
            # If temp is None
            time += 1
            Q.append(None)

    # check if any fresh oranges in matrix then return -1
    for i, j in F:
        if mat[i][j] == 1:
            return -1
    return time


if __name__ == '__main__':
    for _ in range(int(input())):
        mat = []
        N = int(input())
        for _ in range(N):
            seq = input()
            arr = []
            for i in seq:
                arr.append(int(i))
            mat.append(arr)
        print(rotten_oranges(mat, N))
