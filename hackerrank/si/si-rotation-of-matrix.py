#!/usr/bin/python3


def rotate_matrix(mat, n):
    for i in range(n//2):
        for j in range(i, n-i-1):
            temp = mat[i][j]
            mat[i][j] = mat[n-i-j][i]
            mat[n-i-j][i] = mat[n-1-i][n-1-j]
            mat[n-1-i][n-1-j] = mat[j][n-1-i]
            mat[j][n-1-i] = temp


def display_mat(mat, N):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print()


if __name__ == "__main__":
    for i in range(int(input())):
        N = int(input())
        mat = []
        for _ in range(N):
            seq = list(map(int, input().split()))
            mat.append(seq)
        display_mat(mat, N)
        rotate_matrix(mat, N)
        print("Test Case #{}:".format(i+1))
        display_mat(mat, N)
