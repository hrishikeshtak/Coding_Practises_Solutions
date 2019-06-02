#!/usr/bin/python3

# using BFS, find shortest path from source to destination
# prepare binary matrix
# 0: empty cell
# 1: forbidden cell
from collections import deque


def is_safe(mat, i, j, N, M):
    if i >= 0 and j >= 0 and i < N and j < M and mat[i][j] == 0:
        return True
    return False


def print_lexicographically_shortest_path(visited, Si, Sj, Di, Dj, path, dis):
    # backtrack from destination to source in lexicographical order
    # to print path.
    # lexicographical order
    di = [-1, -1, -1,  0, 0,  1, 1, 1]
    dj = [-1,  0,  1, -1, 1, -1, 0, 1]

    if visited[Di][Dj]:
        path.append((Di, Dj))

    if Si == Di and Sj == Dj:
        return True

    for i, j in zip(di, dj):
        row = Di+i
        col = Dj+j
        if is_safe(mat, row, col, N, M) and visited[row][col] is True:
            if dis == 0 and Si == Di and Sj == Dj:
                return True
            # if distance is 0 and source does not matches destination
            elif dis == 0:
                continue
            if print_lexicographically_shortest_path(
                    visited, Si, Sj, row, col, path, dis-1):
                return True
            else:
                path.pop()
    return False


def BFS(mat, queue, visited, Di, Dj, N, M, ans):

    if not queue:
        return False

    x, y, dis = queue.popleft()
    if x == Di and y == Dj:
        visited[x][y] = True
        ans[0] = dis
        return True

    # lexicographical order
    di = [-1, -1, -1,  0, 0,  1, 1, 1]
    dj = [-1,  0,  1, -1, 1, -1, 0, 1]

    size = len(queue)
    for i, j in zip(di, dj):
        row = x+i
        col = y+j
        # print("x: {} y: {} row: {} col: {}".format(x, y, row, col))
        if is_safe(mat, row, col, N, M) and visited[row][col] is False:
            # print(x, y)
            visited[row][col] = True
            queue.append((row, col, dis+1))

    # if queue size is similar to previous size, then that cell
    # does not add any other cell, so it means we can ignore that cell
    if size == len(queue):
        mat[x][y] = 1
        visited[x][y] = False

    if BFS(mat, queue, visited, Di, Dj, N, M, ans):
        return True

    return False


def rat_in_maze(mat, Si, Sj, Di, Dj, N, M):
    queue = deque()

    # visited matrix
    visited = [[False for i in range(M)] for j in range(N)]

    # if source itself is forbidden cell
    if mat[Si][Sj] == 1 or mat[Di][Dj] == 1:
        return -1

    # add Source coordinates + distance in queue
    queue.append((Si, Sj, 0))
    # store visited of Source is True
    visited[Si][Sj] = True
    # store shortest distance
    ans = [0]

    if BFS(mat, queue, visited, Di, Dj, N, M, ans):
        # Path in lexicographical order stored in visited array
        # print("visited: ", visited)
        # print("mat: ", mat)
        print(ans[0])
        if visited:
            path = []
            # print lexicographically shortest path
            if print_lexicographically_shortest_path(
                    visited, Si, Sj, Di, Dj, path, ans[0]):
                # print("path: ", path[::-1])
                path = path[::-1]
                for i in range(0, len(path)):
                    if i == len(path) - 1:
                        print("{},{}".format(path[i][0], path[i][1]), end=" ")
                    else:
                        print("{},{} ->".format(path[i][0], path[i][1]), end=" ")
                print()
        return
    print(-1)


if __name__ == '__main__':
    for _ in range(int(input())):
        N, M, X = map(int, input().split())
        mat = [[0 for i in range(M)] for j in range(N)]
        # source coordinates
        Si, Sj = map(int, input().split())
        # destination coordinates
        Di, Dj = map(int, input().split())
        for _ in range(X):
            # forbidden cell
            i, j = map(int, input().split())
            mat[i][j] = 1
        rat_in_maze(mat, Si, Sj, Di, Dj, N, M)
