#!/usr/bin/python3

# Considering N-8 neighbourhood, your task is to find the number of islands
# in the given landscape.
# Assume that the the 2D matrix is surrounded by water beyond the boundaries.


def no_of_islands(mat, R, C):
    # print(mat)
    cnt = 0
    for i in range(0, R):
        for j in range(0, C):
            if mat[i][j] == 1:
                cnt += 1
                DFS(mat, i, j, R, C)
    return cnt


def valid(i, j, R, C):
    if i < 0 or j < 0 or i >= R or j >= C:
        return False
    return True


def DFS(mat, i, j, R, C):
    # N-8 neighbourhood
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    if valid(i, j, R, C):
        if mat[i][j] == 1:
            mat[i][j] = 0
            for k in range(0, 8):
                DFS(mat, i + di[k], j + dj[k], R, C)


if __name__ == '__main__':
    for _ in range(int(input())):
        mat = []
        R, C = map(int, input().split())
        for _ in range(0, R):
            arr = input()
            row = []
            for i in arr:
                row.append(int(i))
            mat.append(row)
        print(no_of_islands(mat, R, C))
